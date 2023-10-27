package com.nps.example;

public class Player extends Character {

  private float critChance;

  public Player(String name, int hp, int strength, int defense, float critChance) {
    super(name, hp, strength, defense);

    this.critChance = critChance;
  }

  public float getCritChance() {
    return this.critChance;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setCritChance(float critChance) {
    this.critChance = critChance;
  }

  @Override
  public float calculateDmg() {
    return this.strength;
  }
}
