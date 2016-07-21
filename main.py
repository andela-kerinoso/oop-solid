# Test
if __name__ == '__main__':
    import weapon
    from character import Character

    hero = Character('Batman')
    villain = Character('Joker')

    print('{}: {}'.format(hero.name, hero.fight()))
    print('{}: {}\n'.format(villain.name, villain.fight()))

    hero.set_weapon(weapon.Gun())

    print('{}: {}'.format(hero.name, hero.fight()))
    print('{}: {}\n'.format(villain.name, villain.fight()))

    print('{}: {}'.format(villain.name, villain.die()))
