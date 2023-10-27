package com.cgtfarmer.example;

public class Enemy extends Character {

  public Enemy(String name, int hp, int strength, int defense) {
    super(name, hp, strength, defense);
  }

  @Override
  public float calculateDmg() {
    return (this.strength * 0.5f);
  }
}
