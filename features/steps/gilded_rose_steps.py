from behave import given, when, then
from gilded_rose import GildedRose, Item

def init_item(context, name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    context.app = GildedRose(items)
    context.original_sell_in = sell_in
    context.original_quality = quality

@given('an {name} with quality {quality:d} to be sold by {sell_in:d} days')
def step_impl(context, name, quality, sell_in):
    init_item(context, name, sell_in, quality)

@given('an {name} with quality {quality:d} overdue by {overdue:d} days')
def step_impl(context, name, quality, overdue):
    init_item(context, name, -overdue, quality)

@when('a day passes')
def step_impl(context):
    context.app.update_quality()

@then('the quality should be decreased by {decrease:d}')
def step_impl(context, decrease):
    assert context.app.items[0].quality == context.original_quality - decrease

@then('the quality should be increased by {increase:d}')
def step_impl(context, increase):
    assert context.app.items[0].quality == context.original_quality + increase

@then('the quality should be {quality:d}')
def step_impl(context, quality):
    assert context.app.items[0].quality == quality

@then('the quality should remain unchanged')
def step_impl(context):
    assert context.app.items[0].quality == context.original_quality

@then('the sell-by should be decreased by {decrease:d}')
def step_impl(context, decrease):
    assert context.app.items[0].sell_in == context.original_sell_in - decrease

@then('the sell-by should remain unchanged')
def step_impl(context):
    assert context.app.items[0].sell_in == context.original_sell_in
