class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                quality_increase = 0
                if item.sell_in < 6:
                    quality_increase = 3
                elif item.sell_in < 11:
                    quality_increase = 2
                else:
                    quality_increase = 1
                item.quality = min(item.quality + quality_increase, 50)

            elif item.name == "Aged Brie" :
                if item.quality < 50:
                    item.quality += 1

            else:
                if item.quality > 0:
                    item.quality -= 1


            item.sell_in -= 1

            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            item.quality -= 1
                    else:
                        item.quality -= item.quality
                else:
                    if item.quality < 50:
                        item.quality += 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
