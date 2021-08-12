# Created by aleksandrkryzhanovskii at 8/10/21
Feature: Dexcom login test


  Scenario: User can login
    Given Open Main page
    When Click Home User Button
    And Input codechallenge Username
    And Input Password123 Password
    And Click Login Button
    Then Page URL has welcome in it
