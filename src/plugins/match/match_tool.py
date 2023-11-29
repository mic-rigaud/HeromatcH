from PIL import Image
from peewee import fn

from src.bdd.Hero_BDD import Hero


def get_concat_h(im1, im2):
    im3 = Image.open("Heroes/vs.png")
    dst = Image.new('RGB', (im1.width + im2.width + im3.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im3, (im1.width, 0))
    dst.paste(im2, (im1.width + im3.width, 0))
    return dst


def get_image_match(nom1, nom2):
    im1 = Image.open(f"Heroes/{nom1}.png")
    im2 = Image.open(f"Heroes/{nom2}.png")
    get_concat_h(im1, im2).save("data/match_temp.png")
    return "data/match_temp.png"


def get_hero_match():
    return {
        i: {"name": hero.nom, "id": hero.get_id()}
        for i, hero in enumerate(
                Hero.select().order_by(fn.Random()).limit(2), start=1
                )
        }


def ajout_victoire(id_gagnant, id_perdant):
    hero_selected = Hero.get(Hero.id == id_perdant)
    hero_selected.total_match += 1
    hero_selected.save()
    hero_selected = Hero.get(Hero.id == id_gagnant)
    hero_selected.total_point += 1
    hero_selected.total_match += 1
    reponse = f"Victoire pour : {hero_selected.nom}"
    hero_selected.save()
    return reponse
