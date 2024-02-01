Feature: Sulfuras

  Scenario Outline: quality never changes and has never to be sold
    Given an <item> with quality <quality> to be sold by <sell-by> days
    When a day passes
    Then the quality should remain unchanged
    And the sell-by should remain unchanged
    Examples:
      | item                       | quality | sell-by |
      | Sulfuras, Hand of Ragnaros | 80      | 0       |
      | Sulfuras, Hand of Ragnaros | 70      | 1       |
      | Sulfuras, Hand of Ragnaros | 20      | 20      |
