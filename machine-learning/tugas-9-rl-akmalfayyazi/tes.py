import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
import gymnasium as gym
from collections import deque
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
import os

'''
Melatih agen Artificial Intelligence (AI) menggunakan Reinforcement Learning agar jago bermain "CartPole".
Tujuan Utama:
Menyeimbangkan Tiang (Game Goal): Mengajarkan agen untuk menggerakkan kereta (cart) ke kiri atau kanan agar tiang (pole) di atasnya tetap tegak seimbang dan tidak jatuh selama mungkin.

Mencapai Skor Tinggi: Agen belajar secara trial-and-error (menggunakan algoritma PPO) untuk mendapatkan total reward setinggi mungkin (targetnya skor rata-rata di atas 475, yang dianggap "Solved").

Evaluasi Performa: Menghasilkan data statistik dan grafik visual (seperti learning curve) untuk membuktikan bahwa agen semakin pintar seiring berjalannya waktu latihan.
'''

# Set random seeds for reproducibility
def set_seed(seed=42):
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)

# ============================================================================
# OPTIMIZED ACTOR-CRITIC NETWORK
# ============================================================================
class OptimizedActorCritic(nn.Module):
    """Optimized neural network architecture for CartPole"""
    def __init__(self, state_dim, action_dim):
        super(OptimizedActorCritic, self).__init__()
        
        # Larger hidden layers for better representation
        self.shared = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU()
        )
        
        # Separate heads for actor and critic
        self.actor = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim)
        )
        
        self.critic = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )
        
        # Initialize weights properly
        self.apply(self._init_weights)
    
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            nn.init.orthogonal_(module.weight, gain=np.sqrt(2))
            nn.init.constant_(module.bias, 0.0)
    
    def forward(self, state):
        features = self.shared(state)
        action_logits = self.actor(features)
        value = self.critic(features)
        return action_logits, value
    
    def get_action(self, state, deterministic=False):
        with torch.no_grad():
            action_logits, value = self.forward(state)
            dist = Categorical(logits=action_logits)
            
            if deterministic:
                action = torch.argmax(action_logits, dim=-1)
                log_prob = dist.log_prob(action)
            else:
                action = dist.sample()
                log_prob = dist.log_prob(action)
            
            return action, log_prob, value, dist.entropy()

# ============================================================================
# OPTIMIZED PPO AGENT
# ============================================================================
class OptimizedPPOAgent:
    """Highly optimized PPO implementation"""
    def __init__(self, state_dim, action_dim):
        # Optimized hyperparameters for CartPole
        self.gamma = 0.99
        self.gae_lambda = 0.95
        self.clip_epsilon = 0.2
        self.c1 = 0.5  # value loss coefficient
        self.c2 = 0.01  # entropy coefficient
        self.batch_size = 64
        self.n_epochs = 10
        self.max_grad_norm = 0.5
        
        # Network and optimizer
        self.network = OptimizedActorCritic(state_dim, action_dim)
        self.optimizer = optim.Adam(self.network.parameters(), lr=3e-4, eps=1e-5)
        
        # Experience buffer
        self.reset_buffer()
        
    def reset_buffer(self):
        self.buffer = {
            'states': [],
            'actions': [],
            'rewards': [],
            'values': [],
            'log_probs': [],
            'dones': [],
            'entropies': []
        }
    
    def store(self, state, action, reward, value, log_prob, done, entropy):
        self.buffer['states'].append(state)
        self.buffer['actions'].append(action)
        self.buffer['rewards'].append(reward)
        self.buffer['values'].append(value)
        self.buffer['log_probs'].append(log_prob)
        self.buffer['dones'].append(done)
        self.buffer['entropies'].append(entropy)
    
    def compute_gae(self, next_value):
        """Compute Generalized Advantage Estimation"""
        rewards = self.buffer['rewards']
        values = self.buffer['values'] + [next_value]
        dones = self.buffer['dones']
        
        advantages = []
        gae = 0
        
        for t in reversed(range(len(rewards))):
            delta = rewards[t] + self.gamma * values[t+1] * (1-dones[t]) - values[t]
            gae = delta + self.gamma * self.gae_lambda * (1-dones[t]) * gae
            advantages.insert(0, gae)
        
        returns = [adv + val for adv, val in zip(advantages, values[:-1])]
        return advantages, returns
    
    def update(self):
        """Update policy with collected experience"""
        # Get next value for GAE
        with torch.no_grad():
            last_state = torch.FloatTensor(self.buffer['states'][-1]).unsqueeze(0)
            _, next_value = self.network(last_state)
            next_value = next_value.item()
        
        # Compute advantages and returns
        advantages, returns = self.compute_gae(next_value)
        
        # Convert to tensors
        states = torch.FloatTensor(np.array(self.buffer['states']))
        actions = torch.LongTensor(self.buffer['actions'])
        old_log_probs = torch.FloatTensor(self.buffer['log_probs'])
        advantages = torch.FloatTensor(advantages)
        returns = torch.FloatTensor(returns)
        
        # Normalize advantages
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
        
        # Training metrics
        metrics = {
            'policy_loss': 0,
            'value_loss': 0,
            'entropy': 0,
            'total_loss': 0,
            'approx_kl': 0,
            'clipfrac': 0
        }
        n_updates = 0
        
        # Multiple epochs of updates
        for epoch in range(self.n_epochs):
            # Mini-batch training
            indices = np.random.permutation(len(states))
            
            for start in range(0, len(states), self.batch_size):
                end = start + self.batch_size
                batch_idx = indices[start:end]
                
                # Get batch data
                batch_states = states[batch_idx]
                batch_actions = actions[batch_idx]
                batch_old_log_probs = old_log_probs[batch_idx]
                batch_advantages = advantages[batch_idx]
                batch_returns = returns[batch_idx]
                
                # Forward pass
                action_logits, values = self.network(batch_states)
                dist = Categorical(logits=action_logits)
                log_probs = dist.log_prob(batch_actions)
                entropy = dist.entropy().mean()
                
                # Policy loss (PPO clipped objective)
                ratio = torch.exp(log_probs - batch_old_log_probs)
                surr1 = ratio * batch_advantages
                surr2 = torch.clamp(ratio, 1-self.clip_epsilon, 1+self.clip_epsilon) * batch_advantages
                policy_loss = -torch.min(surr1, surr2).mean()
                
                # Value loss (clipped)
                values = values.squeeze()
                value_loss = nn.MSELoss()(values, batch_returns)
                
                # Total loss
                loss = policy_loss + self.c1 * value_loss - self.c2 * entropy
                
                # Backward pass
                self.optimizer.zero_grad()
                loss.backward()
                nn.utils.clip_grad_norm_(self.network.parameters(), self.max_grad_norm)
                self.optimizer.step()
                
                # Track metrics
                with torch.no_grad():
                    approx_kl = (batch_old_log_probs - log_probs).mean().item()
                    clipfrac = torch.mean((torch.abs(ratio - 1) > self.clip_epsilon).float()).item()
                
                metrics['policy_loss'] += policy_loss.item()
                metrics['value_loss'] += value_loss.item()
                metrics['entropy'] += entropy.item()
                metrics['total_loss'] += loss.item()
                metrics['approx_kl'] += approx_kl
                metrics['clipfrac'] += clipfrac
                n_updates += 1
        
        # Average metrics
        for key in metrics:
            metrics[key] /= n_updates
        
        # Reset buffer
        self.reset_buffer()
        
        return metrics

# ============================================================================
# OPTIMIZED TRAINER
# ============================================================================
class OptimizedTrainer:
    """Optimized training loop for fast convergence"""
    def __init__(self, env_name='CartPole-v1', max_episodes=600, seed=42):
        self.env_name = env_name
        self.env = gym.make(env_name)
        self.max_episodes = max_episodes
        self.seed = seed
        
        # Get environment specs
        self.state_dim = self.env.observation_space.shape[0]
        self.action_dim = self.env.action_space.n
        
        # Create agent
        self.agent = OptimizedPPOAgent(self.state_dim, self.action_dim)
        
        # Training parameters
        self.update_frequency = 2048  # Update after this many steps
        self.eval_frequency = 20
        self.n_eval_episodes = 10
        
        # Metrics
        self.episode_rewards = []
        self.episode_lengths = []
        self.eval_rewards = []
        self.training_metrics = []
        
        # Best model tracking
        self.best_eval_reward = -float('inf')
        
        # Create directories
        self.save_dir = f"optimized_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(self.save_dir, exist_ok=True)
        
    def train(self):
        """Main training loop"""
        set_seed(self.seed)
        self.env.reset(seed=self.seed)
        
        state, _ = self.env.reset()
        episode_reward = 0
        episode_length = 0
        total_steps = 0
        
        print(f"🚀 Starting Optimized Training on {self.env_name}")
        print(f"State dim: {self.state_dim}, Action dim: {self.action_dim}\n")
        
        for episode in range(self.max_episodes):
            episode_reward = 0
            episode_length = 0
            state, _ = self.env.reset()
            done = False
            
            while not done:
                # Get action
                state_tensor = torch.FloatTensor(state).unsqueeze(0)
                action, log_prob, value, entropy = self.agent.network.get_action(state_tensor)
                
                # Take step
                next_state, reward, terminated, truncated, _ = self.env.step(action.item())
                done = terminated or truncated
                
                # Store transition
                self.agent.store(
                    state, action.item(), reward, 
                    value.item(), log_prob.item(), done, entropy.item()
                )
                
                state = next_state
                episode_reward += reward
                episode_length += 1
                total_steps += 1
                
                # Update policy
                if total_steps % self.update_frequency == 0 and len(self.agent.buffer['states']) > 0:
                    metrics = self.agent.update()
                    self.training_metrics.append(metrics)
            
            # Store episode metrics
            self.episode_rewards.append(episode_reward)
            self.episode_lengths.append(episode_length)
            
            # Logging
            if (episode + 1) % 10 == 0:
                avg_reward = np.mean(self.episode_rewards[-10:])
                avg_length = np.mean(self.episode_lengths[-10:])
                print(f"Episode {episode+1:4d} | Avg Reward: {avg_reward:7.2f} | Avg Length: {avg_length:6.1f}")
            
            # Evaluation
            if (episode + 1) % self.eval_frequency == 0:
                eval_reward = self.evaluate()
                self.eval_rewards.append((episode + 1, eval_reward))
                print(f"{'='*70}")
                print(f"📊 EVALUATION at Episode {episode+1}: {eval_reward:.2f}")
                print(f"{'='*70}\n")
                
                # Save best model
                if eval_reward > self.best_eval_reward:
                    self.best_eval_reward = eval_reward
                    self.save_model('best_model.pt')
                    print(f"💾 New best model saved! Eval reward: {eval_reward:.2f}\n")
        
        self.env.close()
        return self.get_stats()
    
    def evaluate(self, render=False):
        """Evaluate current policy"""
        eval_rewards = []
        
        for _ in range(self.n_eval_episodes):
            state, _ = self.env.reset()
            episode_reward = 0
            done = False
            
            while not done:
                state_tensor = torch.FloatTensor(state).unsqueeze(0)
                action, _, _, _ = self.agent.network.get_action(state_tensor, deterministic=True)
                state, reward, terminated, truncated, _ = self.env.step(action.item())
                done = terminated or truncated
                episode_reward += reward
            
            eval_rewards.append(episode_reward)
        
        return np.mean(eval_rewards)
    
    def save_model(self, filename):
        """Save model checkpoint"""
        path = os.path.join(self.save_dir, filename)
        torch.save({
            'model_state_dict': self.agent.network.state_dict(),
            'optimizer_state_dict': self.agent.optimizer.state_dict(),
            'best_eval_reward': self.best_eval_reward,
        }, path)
    
    def get_stats(self):
        """Return training statistics"""
        return {
            'episode_rewards': self.episode_rewards,
            'episode_lengths': self.episode_lengths,
            'eval_rewards': self.eval_rewards,
            'training_metrics': self.training_metrics
        }

def to_python(obj):
    import numpy as np

    if isinstance(obj, dict):
        return {k: to_python(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_python(v) for v in obj]
    if isinstance(obj, np.generic):
        return obj.item()
    return obj

# ============================================================================
# COMPREHENSIVE EVALUATOR
# ============================================================================
class ComprehensiveEvaluator:
    """Generate detailed evaluation report"""
    def __init__(self, stats, save_dir):
        self.stats = stats
        self.save_dir = save_dir
        
    def generate_full_report(self):
        """Generate all visualizations and metrics"""
        print("\n" + "="*70)
        print("📈 GENERATING COMPREHENSIVE EVALUATION REPORT")
        print("="*70 + "\n")
        
        self.plot_learning_curves()
        self.plot_advanced_metrics()
        metrics = self.compute_detailed_metrics()
        self.save_metrics(metrics)
        self.print_report(metrics)
        
        return metrics
    
    def plot_learning_curves(self):
        """Plot beautiful learning curves"""
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        
        rewards = self.stats['episode_rewards']
        lengths = self.stats['episode_lengths']
        
        # 1. Episode Rewards with Moving Average
        window = 50
        if len(rewards) > window:
            ma = np.convolve(rewards, np.ones(window)/window, mode='valid')
            axes[0, 0].plot(rewards, alpha=0.3, color='lightblue', label='Raw')
            axes[0, 0].plot(range(window-1, len(rewards)), ma, color='darkblue', 
                           linewidth=2, label=f'MA-{window}')
        else:
            axes[0, 0].plot(rewards, color='darkblue')
        axes[0, 0].set_xlabel('Episode', fontsize=11)
        axes[0, 0].set_ylabel('Reward', fontsize=11)
        axes[0, 0].set_title('Episode Rewards Over Time', fontsize=12, fontweight='bold')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. Evaluation Rewards
        if self.stats['eval_rewards']:
            eval_eps, eval_rews = zip(*self.stats['eval_rewards'])
            axes[0, 1].plot(eval_eps, eval_rews, marker='o', markersize=8, 
                           linewidth=2, color='green')
            axes[0, 1].axhline(y=475, color='r', linestyle='--', 
                              label='Solved Threshold (475)')
            axes[0, 1].set_xlabel('Episode', fontsize=11)
            axes[0, 1].set_ylabel('Mean Reward', fontsize=11)
            axes[0, 1].set_title('Evaluation Performance', fontsize=12, fontweight='bold')
            axes[0, 1].legend()
            axes[0, 1].grid(True, alpha=0.3)
        
        # 3. Episode Lengths
        if len(lengths) > window:
            ma_len = np.convolve(lengths, np.ones(window)/window, mode='valid')
            axes[0, 2].plot(lengths, alpha=0.3, color='lightcoral')
            axes[0, 2].plot(range(window-1, len(lengths)), ma_len, 
                           color='darkred', linewidth=2)
        else:
            axes[0, 2].plot(lengths, color='darkred')
        axes[0, 2].set_xlabel('Episode', fontsize=11)
        axes[0, 2].set_ylabel('Length', fontsize=11)
        axes[0, 2].set_title('Episode Lengths', fontsize=12, fontweight='bold')
        axes[0, 2].grid(True, alpha=0.3)
        
        # 4. Reward Distribution
        axes[1, 0].hist(rewards, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
        axes[1, 0].axvline(np.mean(rewards), color='r', linestyle='--', 
                          linewidth=2, label=f'Mean: {np.mean(rewards):.1f}')
        axes[1, 0].axvline(np.median(rewards), color='g', linestyle='--', 
                          linewidth=2, label=f'Median: {np.median(rewards):.1f}')
        axes[1, 0].set_xlabel('Reward', fontsize=11)
        axes[1, 0].set_ylabel('Frequency', fontsize=11)
        axes[1, 0].set_title('Reward Distribution', fontsize=12, fontweight='bold')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # 5. Training Metrics
        if self.stats['training_metrics']:
            policy_losses = [m['policy_loss'] for m in self.stats['training_metrics']]
            value_losses = [m['value_loss'] for m in self.stats['training_metrics']]
            
            ax2 = axes[1, 1]
            ax2.plot(policy_losses, label='Policy Loss', color='blue', alpha=0.7)
            ax2.plot(value_losses, label='Value Loss', color='red', alpha=0.7)
            ax2.set_xlabel('Update Step', fontsize=11)
            ax2.set_ylabel('Loss', fontsize=11)
            ax2.set_title('Training Losses', fontsize=12, fontweight='bold')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
        
        # 6. Progress Indicator
        splits = 5
        split_size = len(rewards) // splits
        split_means = [np.mean(rewards[i*split_size:(i+1)*split_size]) 
                      for i in range(splits)]
        
        axes[1, 2].bar(range(1, splits+1), split_means, color='teal', alpha=0.7)
        axes[1, 2].plot(range(1, splits+1), split_means, marker='o', 
                       color='darkred', linewidth=2, markersize=8)
        axes[1, 2].set_xlabel('Training Phase', fontsize=11)
        axes[1, 2].set_ylabel('Mean Reward', fontsize=11)
        axes[1, 2].set_title('Learning Progress by Phase', fontsize=12, fontweight='bold')
        axes[1, 2].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'comprehensive_analysis.png'), 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Learning curves saved!")
    
    def plot_advanced_metrics(self):
        """Plot advanced performance metrics"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        rewards = np.array(self.stats['episode_rewards'])
        
        # Rolling statistics
        window = 100
        if len(rewards) >= window:
            rolling_mean = []
            rolling_std = []
            
            for i in range(window, len(rewards)+1):
                rolling_mean.append(np.mean(rewards[i-window:i]))
                rolling_std.append(np.std(rewards[i-window:i]))
            
            x = range(window, len(rewards)+1)
            rolling_mean = np.array(rolling_mean)
            rolling_std = np.array(rolling_std)
            
            axes[0].plot(x, rolling_mean, color='blue', linewidth=2, label='Mean')
            axes[0].fill_between(x, rolling_mean-rolling_std, rolling_mean+rolling_std, 
                                alpha=0.3, color='blue', label='±1 Std')
            axes[0].axhline(y=475, color='r', linestyle='--', 
                          linewidth=2, label='Solved (475)')
            axes[0].set_xlabel('Episode', fontsize=11)
            axes[0].set_ylabel('Reward', fontsize=11)
            axes[0].set_title(f'Rolling Statistics (window={window})', 
                            fontsize=12, fontweight='bold')
            axes[0].legend()
            axes[0].grid(True, alpha=0.3)
        
        # Success rate over time
        threshold = 475
        window = 50
        if len(rewards) >= window:
            success_rates = []
            for i in range(window, len(rewards)+1):
                success_rate = np.mean(rewards[i-window:i] >= threshold)
                success_rates.append(success_rate * 100)
            
            axes[1].plot(range(window, len(rewards)+1), success_rates, 
                        color='green', linewidth=2)
            axes[1].axhline(y=95, color='r', linestyle='--', 
                          linewidth=2, label='95% Success')
            axes[1].set_xlabel('Episode', fontsize=11)
            axes[1].set_ylabel('Success Rate (%)', fontsize=11)
            axes[1].set_title(f'Success Rate Over Time (threshold={threshold})', 
                            fontsize=12, fontweight='bold')
            axes[1].legend()
            axes[1].grid(True, alpha=0.3)
            axes[1].set_ylim([0, 105])
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'advanced_metrics.png'), 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Advanced metrics saved!")
    
    def compute_detailed_metrics(self):
        """Compute comprehensive metrics"""
        rewards = np.array(self.stats['episode_rewards'])
        
        # Overall statistics
        overall_mean = np.mean(rewards)
        overall_std = np.std(rewards)
        overall_median = np.median(rewards)
        overall_min = np.min(rewards)
        overall_max = np.max(rewards)
        
        # Final performance (last 100 episodes)
        final_rewards = rewards[-100:] if len(rewards) > 100 else rewards
        final_mean = np.mean(final_rewards)
        final_std = np.std(final_rewards)
        final_median = np.median(final_rewards)
        
        # Success metrics
        threshold_475 = np.mean(rewards >= 475) * 100
        threshold_450 = np.mean(rewards >= 450) * 100
        threshold_400 = np.mean(rewards >= 400) * 100
        
        # Learning speed
        first_quarter = rewards[:len(rewards)//4]
        last_quarter = rewards[3*len(rewards)//4:]
        improvement = (np.mean(last_quarter) - np.mean(first_quarter)) / np.mean(first_quarter) * 100
        
        # Stability (coefficient of variation)
        cv_overall = (overall_std / overall_mean) * 100 if overall_mean > 0 else 0
        cv_final = (final_std / final_mean) * 100 if final_mean > 0 else 0
        
        metrics = {
            'overall_mean': overall_mean,
            'overall_std': overall_std,
            'overall_median': overall_median,
            'overall_min': overall_min,
            'overall_max': overall_max,
            'final_mean': final_mean,
            'final_std': final_std,
            'final_median': final_median,
            'success_rate_475': threshold_475,
            'success_rate_450': threshold_450,
            'success_rate_400': threshold_400,
            'improvement_percentage': improvement,
            'cv_overall': cv_overall,
            'cv_final': cv_final,
            'total_episodes': len(rewards),
            'solved': final_mean >= 475
        }
        
        return metrics

    def save_metrics(self, metrics):
        path = os.path.join(self.save_dir, 'evaluation_metrics.json')
        with open(path, 'w') as f:
            json.dump(to_python(metrics), f, indent=4)
        print(f"✅ Metrics saved to {path}")
    
    def print_report(self, metrics):
        """Print beautiful evaluation report"""
        print("\n" + "="*70)
        print("🎯 FINAL EVALUATION REPORT - CartPole-v1")
        print("="*70)
        
        print("\n📊 OVERALL PERFORMANCE:")
        print(f"  Mean Reward ..................... {metrics['overall_mean']:.2f}")
        print(f"  Std Deviation ................... {metrics['overall_std']:.2f}")
        print(f"  Median Reward ................... {metrics['overall_median']:.2f}")
        print(f"  Min/Max Reward .................. {metrics['overall_min']:.0f} / {metrics['overall_max']:.0f}")
        
        print("\n🏆 FINAL PERFORMANCE (Last 100 Episodes):")
        print(f"  Mean Reward ..................... {metrics['final_mean']:.2f}")
        print(f"  Std Deviation ................... {metrics['final_std']:.2f}")
        print(f"  Median Reward ................... {metrics['final_median']:.2f}")
        
        print("\n✅ SUCCESS RATES:")
        print(f"  Episodes >= 475 (Solved) ........ {metrics['success_rate_475']:.1f}%")
        print(f"  Episodes >= 450 ................. {metrics['success_rate_450']:.1f}%")
        print(f"  Episodes >= 400 ................. {metrics['success_rate_400']:.1f}%")
        
        print("\n📈 LEARNING DYNAMICS:")
        print(f"  Improvement (First→Last Quarter). {metrics['improvement_percentage']:.1f}%")
        print(f"  CV Overall ...................... {metrics['cv_overall']:.1f}%")
        print(f"  CV Final ........................ {metrics['cv_final']:.1f}%")
        
        print("\n🎮 TRAINING INFO:")
        print(f"  Total Episodes .................. {metrics['total_episodes']}")
        print(f"  Environment Solved? ............. {'YES ✅' if metrics['solved'] else 'NO ❌'}")
        
        # Performance rating
        if metrics['final_mean'] >= 475:
            rating = "⭐⭐⭐⭐⭐ EXCELLENT - Solved!"
        elif metrics['final_mean'] >= 450:
            rating = "⭐⭐⭐⭐ VERY GOOD - Near Solved"
        elif metrics['final_mean'] >= 400:
            rating = "⭐⭐⭐ GOOD - Strong Performance"
        elif metrics['final_mean'] >= 300:
            rating = "⭐⭐ FAIR - Learning Well"
        else:
            rating = "⭐ NEEDS IMPROVEMENT"
        
        print(f"\n🏅 OVERALL RATING: {rating}")
        print("="*70 + "\n")

# ============================================================================
# MAIN EXECUTION
# ============================================================================
def main():
    """Run optimized training and evaluation"""
    print("="*70)
    print("🚀 OPTIMIZED REINFORCEMENT LEARNING TRAINING")
    print("="*70 + "\n")
    
    # Create trainer
    trainer = OptimizedTrainer(
        env_name='CartPole-v1',
        max_episodes=600,
        seed=42
    )
    
    # Train
    stats = trainer.train()
    
    # Comprehensive evaluation
    evaluator = ComprehensiveEvaluator(stats, trainer.save_dir)
    metrics = evaluator.generate_full_report()
    
    print(f"\n✅ All results saved to: {trainer.save_dir}/")
    print("="*70)
    
    return trainer, stats, metrics

if __name__ == "__main__":
    trainer, stats, metrics = main()