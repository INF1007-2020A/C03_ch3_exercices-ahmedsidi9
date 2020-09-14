#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    average=(a*b*C)/3
    return average


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_radians1=(pi*angle_degs)/180
    angle_radians2=(pi*(angle_mins*60))/180
    angle_radians3=(pi*(anglee_seca*60*60))/180
    return angle_radians
    


def to_degrees(angle_rads: float) -> tuple:
    angle_degrees=(180*angle_rads)/pi
    angle_minutes=angle_degrees/60
    angle_secondes=angle_minute/60
    return angle_rads, angle_minute, angle_seconde


def to_celsius(temperature: float) -> float:
    angle_celsius=(temperature-32)*(5/9)
    return angle_celsius


def to_farenheit(temperature: float) -> float:
    angle_farenheit=(temperature*(9/5))-32
    return angle_farenheit


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
