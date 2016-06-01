Feature: Print tweets
    In order to play with Lettuce
    As beginners
    We'll implement print tweets

    Scenario: Print 10 tweets
        Given I have the number 10
        When I search the tweets
        Then I see tweets 10