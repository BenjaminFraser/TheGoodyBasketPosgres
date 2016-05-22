#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('postgresql:///thegoodybasket')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='profile1.jpg')
session.add(User1)
session.commit()

User2 = User(name="Lisa Rodriguez", email="lisarodriguez@gmail.com",
             picture='profile2.jpg')
session.add(User2)
session.commit()

User3 = User(name="Hannah Martin", email="Hanzzymartin@hotmail.com",
             picture='profile3.jpg')
session.add(User3)
session.commit()

User4 = User(name="Brad Phillips", email="Bradistheboss@gmail.com",
             picture='profile4.jpg')
session.add(User4)
session.commit()

User5 = User(name="Marv Robins", email="Marvis1234rop@hotmail.com",
             picture='profile5.jpg')
session.add(User5)
session.commit()

User6 = User(name="Jennifer Andrews", email="JennAndrews5426@gmail.com",
             picture='profile6.jpg')
session.add(User6)
session.commit()

# items for Snowboarding
category1 = Category(user_id=1, name="Snowboarding")

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="White Snowboard", description="Brand new white 145cm pro model. Also available in red, orange and grey.",
                     price="$250.00", picture="snowboard_white.jpg", category=category1)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=1, name="Snow Jacket", description="Warm and puffy red snow jacket. Perfect for keeping warm!",
                     price="$199.99", picture="jacket.jpg", category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Snow Goggles", description="Brand new 2015 model anti-glare, removable lens and adjustable strap goggles.",
                     price="$49.99", picture="snow_goggles.jpg", category=category1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Snow Gloves", description="Thick and padded snow gloves to keep toasty hands. Available in red and black.",
                     price="$39.99", picture="ski_gloves.jpg", category=category1)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=1, name="Snow Hat", description="Keep your head warm with this knitted-by-hand snow hat.",
                     price="$17.99", picture="warm_hat.jpg", category=category1)

session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(user_id=1, name="Ray-Ban Aviators", description="Keep cool on the slopes with these huge aviators.",
                     price="$1.99", picture="ray_bans.jpg", category=category1)

session.add(categoryItem6)
session.commit()


# Items for Skiing
category2 = Category(user_id=2, name="Skiing")

session.add(category2)
session.commit()


categoryItem1 = CategoryItem(user_id=2, name="Ski Boots", description="Warm, lightweight and super rugged ski boots. Available in all sizes.",
                     price="$175.50", picture="ski_boots.jpg", category=category2)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=2, name="Ski Gloves", description="Padded and warm waterproof gloves, available in red and black.",
                     price="$52.99", picture="ski_gloves.jpg", category=category2)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=2, name="K2 Soloman Skis", description="Brand new 2015 Solomon K2 skis in size 175.",
                     price="$450.00", picture="k2_skis.jpg", category=category2)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=2, name="Walking Boots", description="Warm and weatherproof. Available in all sizes.",
                     price="$69.99", picture="walking_boots.jpg", category=category2)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=2, name="Enhanced walking boots", description="Made with grade A beef",
                     price="$7.99", picture="walking_boots.jpg", category=category2)

session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(user_id=2, name="Gold plated walking boots", description="16oz of refreshing goodness",
                     price="$1.99", picture="walking_boots.jpg", category=category2)

session.add(categoryItem6)
session.commit()


# Items for Laptops
category3 = Category(user_id=3, name="Laptops")

session.add(category3)
session.commit()


categoryItem1 = CategoryItem(user_id=3, name="Retina MacBook Pro 13 inch", description="MacBook Pro 13-inch dual-core i5 2.5GHz/4GB/500GB/HD Graphics 4000/SD",
                     price="$999.00", picture="macbook.jpg", category=category3)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=3, name="Microsoft Surface Pro 3", description="Microsoft Surface Pro 3 256GB Silver tablet with keyboard.",
                     price="$799.99", picture="surface_pro.jpg", category=category3)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=3, name="Sony Vaio", description="Sony Vaio VPCX13C7E Notebook Intel Atom (Z540).",
                     price="$5.50", picture="sony_vaio.jpg", category=category3)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=3, name="Sony Vaio Mk 2", description="fresh baked and served with ice cream",
                     price="$3.99", picture="sony_vaio.jpg", category=category3)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=3, name="Enhanced Sony Vaio", description="Made with grade A beef instead of silicon chips.",
                     price="$7.99", picture="sony_vaio.jpg", category=category3)

session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(user_id=3, name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", picture="sony_vaio.jpg", category=category3)

session.add(categoryItem6)
session.commit()


# Items for biking category.
category4 = Category(user_id=4, name="Biking")

session.add(category4)
session.commit()


categoryItem1 = CategoryItem(user_id=4, name="Racing Bike", description="Feel the speed with this super light and stiff carbon fibre racing bike.",
                     price="$1499.99", picture="racing_bike.jpg", category=category4)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=4, name="Bike Helmet", description="Protect your head from falls with a super strong helmet.",
                     price="$22.99", picture="bike_helmet.jpg", category=category4)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=4, name="Bike Chain", description="Spare chain with a full range of sizes and types available.",
                     price="$15.50", picture="bike_chain.jpg", category=category4)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=4, name="27 Inch Tyre", description="A wonderfully resistant tyre with Smart Guard protection.",
                     price="$33.99", picture="bike_tyres.jpg", category=category4)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=4, name="Puncture Repair Kit", description="Part of the essentials list when preparing for a bike ride.",
                     price="$15.99", picture="puncture_repair_kit.jpg", category=category4)

session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(user_id=4, name="White Stripe Crash Helmet", description="Colourful and stylish streamlined biking helmet.",
                     price="$29.99", picture="bike_helmet2.jpg", category=category4)

session.add(categoryItem6)
session.commit()


# Items for surfing category.
category5 = Category(user_id=5, name="Surfing")

session.add(category5)
session.commit()


categoryItem1 = CategoryItem(user_id=5, name="Surf Wax", description="Essential surfboard traction.",
                     price="$7.50", picture="surf_wax.jpg", category=category5)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=5, name="Surfboard", description="This versatile shape will glide you through the waves.",
                     price="$299.99", picture="surfboard.jpg", category=category5)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=5, name="Wetsuit", description="Keep warm and protected in the cold months.",
                     price="$150.00", picture="wetsuit.jpg", category=category5)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=5, name="Flip Flops", description="Blue, easy fit slip on.",
                     price="$3.99", picture="flip_flops.jpg", category=category5)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=5, name="Hat", description="Hat for chilling in the beach sun.",
                     price="$7.99", picture="flip_flops.jpg", category=category5)

session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(user_id=5, name="Root Beer soaked flip-flops", description="16oz of refreshing goodness poured over a fresh set of flip-flops",
                     price="$1.99", picture="flip_flops.jpg", category=category5)

session.add(categoryItem6)
session.commit()

print "Added Category items and users!"