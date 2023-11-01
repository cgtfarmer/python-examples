package com.cgtfarmer.example;

abstract class Character {

  protected String name;
  protected int strength;

  private int hp;
  private int defense;

  public Character(String name, int hp, int strength, int defense) {
    this.name = name;
    this.hp = hp;
    this.strength = strength;
    this.defense = defense;
  }

  public String getName() {
    return this.name;
  }

  public int getHp() {
    return this.hp;
  }

  public int getStrength() {
    return this.strength;
  }

  public int getDefense() {
    return this.defense;
  }

  public void setHp(int hp) {
    this.hp = hp;
  }

  public void setStrength(int strength) {
    this.strength = strength;
  }

  public void setDefense(int defense) {
    this.defense = defense;
  }

  public float calculateDmg() throws Exception {
    throw new Exception("Must override this method");
  }

  // public void thingy() {
  //   int x = 5;
  //   System.out.println(x);

  //   String name = "John";
  //   System.out.println(name);

  //   String fullName = name + " Doe";
  //   System.out.println(fullName);
  // }

  public String toString() {
    return "name=" + this.name + " hp=" + this.hp + " strength=" + this.strength + " defense=" + this.defense;
  }
}
