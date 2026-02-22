# tests/test_ball_update.py
import pytest
from src.ball import Ball
from src.ball_area import BallArea

def test_ball_update_moves_position():
    ball = Ball(
        x=100,
        y=100,
        radius=10,
        color=(255, 0, 0),
        speed_x=5,
        speed_y=-3,
    )

    ball.update()

    assert ball.x == 105
    assert ball.y == 97

def test_ball_bounce_left_and_right_walls():
    area = BallArea(
        min_x=50,
        min_y=50,
        max_x=150,
        max_y=150,
    )

    # Bola dekat dinding kiri, bergerak ke kiri
    ball = Ball(
        x=55,
        y=100,
        radius=10,
        color=(255, 255, 255),
        speed_x=-5,
        speed_y=0,
    )

    ball.collide_with_walls(area)

    # Karena posisi + radius melampaui batas kiri, speed_x harus terbalik
    assert ball.speed_x == 5
    assert ball.speed_y == 0


def test_ball_bounce_top_and_bottom_walls():
    area = BallArea(
        min_x=50,
        min_y=50,
        max_x=150,
        max_y=150,
    )

    # Bola dekat dinding atas, bergerak ke atas
    ball = Ball(
        x=100,
        y=55,
        radius=10,
        color=(255, 255, 255),
        speed_x=0,
        speed_y=-4,
    )

    ball.collide_with_walls(area)

    assert ball.speed_x == 0
    assert ball.speed_y == 4

def test_ball_collision_changes_both_velocities():
    ball1 = Ball(
        x=100,
        y=100,
        radius=10,
        color=(255, 0, 0),
        speed_x=3,
        speed_y=0,
    )

    ball2 = Ball(
        x=110,  # cukup dekat untuk tabrakan (jarak 10, radius total 20)
        y=100,
        radius=10,
        color=(0, 255, 0),
        speed_x=-2,
        speed_y=1,
    )

    ball1.collide_with_ball(ball2)

    # Dalam implementasi sederhana: kecepatan kedua bola dibalik
    assert ball1.speed_x == -3
    assert ball1.speed_y == 0
    assert ball2.speed_x == 2
    assert ball2.speed_y == -1


def test_ball_no_collision_no_velocity_change():
    ball1 = Ball(
        x=100,
        y=100,
        radius=10,
        color=(255, 0, 0),
        speed_x=3,
        speed_y=0,
    )

    ball2 = Ball(
        x=200,  # jauh (jarak 100, radius total 20) → tidak tabrakan
        y=100,
        radius=10,
        color=(0, 255, 0),
        speed_x=-2,
        speed_y=1,
    )

    ball1.collide_with_ball(ball2)

    assert ball1.speed_x == 3
    assert ball1.speed_y == 0
    assert ball2.speed_x == -2
    assert ball2.speed_y == 1