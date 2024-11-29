
# Table of Contents

1.  [Project](#org59e961f)
    1.  [Root](#org16ce9f0)
2.  [Game](#org066b609)
    1.  [Overview](#orgc96d584)
    2.  [Team](#org60de0c8)
    3.  [Gameplay](#org935f007)
    4.  [Story](#orgd64e211)
    5.  [Art and Aesthetics](#org3174104)
    6.  [Sound and Music](#org59ec1ae)
    7.  [Marketing and Release](#org684357e)
    8.  [Post-Launch](#orge7fb754)
    9.  [Miscellaneous](#org068f782)
    10. [notes](#org16a2db1)
3.  [Links](#orgb54cbe8)
    1.  [VSCodium](#org1b99a9d)
    2.  [org-mode](#org24cd079)



<a id="org59e961f"></a>

# TODO Project

just an overall view of directory structure


<a id="org16ce9f0"></a>

## Root


### assets

-   images
-   sounds
-   etc


### data

-   game data
-   save states
-   settings
-   config


### planetclicker

main source code for game

1.  \`\_<sub>init</sub>\_<sub>.py</sub>\`

2.  \`\_<sub>main</sub>\_<sub>.py</sub>\`


<a id="org066b609"></a>

# Game


<a id="orgc96d584"></a>

## Overview

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">title</td>
<td class="org-left">Planet Clicker</td>
</tr>

<tr>
<td class="org-left">genres</td>
<td class="org-left">clicker, idler, strategy</td>
</tr>

<tr>
<td class="org-left">platforms</td>
<td class="org-left">steam (win, mac, linux), android?</td>
</tr>

<tr>
<td class="org-left">audiences</td>
<td class="org-left">casual</td>
</tr>

<tr>
<td class="org-left">summary</td>
<td class="org-left">?</td>
</tr>
</tbody>
</table>


<a id="org60de0c8"></a>

## Team

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">name</td>
<td class="org-left">role</td>
</tr>

<tr>
<td class="org-left">adam</td>
<td class="org-left">ice cream</td>
</tr>

<tr>
<td class="org-left">ben</td>
<td class="org-left">telekinesis</td>
</tr>
</tbody>
</table>


<a id="org935f007"></a>

## Gameplay


### TODO Core Mechanics

*Describe the main mechanics that players will engage with.*
*Highlight what makes these mechanics unique.*

-   start by clicking to generate **mana**
    -   have a resource counter that tracks mana
-   purchase planets/etc
    -   **planets** can automatically generate mana
-   upgrade sun, planets, click, etc
    -   sun can be upgraded to reduce cycle time (how long takes each planet to generate mana)
    -   planets can be upgraded in various ways
    -   click can be upgraded to increase the amount of resources obtained per click or over time.
-   unlock new areas, abilities, etc?
-   occasionally waves of enemies may spawn
-   player can purchase items such as new suns, skins, etc


### Strategy

-   must decide how to best spend their resources; eg, balancing between upgrading click power versus automation
-   timing of purchasing upgrades


### TODO Game Loop

*Explain the cycle of actions players will take.*
*What do players do repeatedly?*


### TODO Progression

How do players progress? (levels, experience, items)
Mention any leveling systems, skill trees, etc.


### TODO Difficulty

-   Describe how difficulty scales throughout the game.
-   Include any dynamic difficulty adjustments if applicable.


<a id="orgd64e211"></a>

## Story


### TODO Narrative Overview

-   Summary of the game&rsquo;s story and themes.


### TODO Setting

-   Describe the game world, time period, and notable locations.


### TODO Characters

-   List main characters and their roles in the story.
-   Include a brief description and motivations for each character.


<a id="org3174104"></a>

## Art and Aesthetics


### TODO Art Style

-   Describe the

visual style (2D, 3D, pixel art, etc.)


### TODO Mood and Tone

-   Discuss the mood of the game (light-hearted, dark, comedic, etc.)


### User Interface

-   display various metrics clearly, enabling players to track their progress, understand resource generation rates, and make informed decisions about upgrades.
-   bright, colorful graphics, animations, and sound effects to provide immediate feedback and satisfaction from clicking or earning resources.


<a id="org59ec1ae"></a>

## Sound and Music


### TODO Sound Design

-   Talk about sound effects, ambiance, and how they enhance gameplay.


### TODO Music

-   Discuss themes or styles of music used throughout the game.


<a id="org684357e"></a>

## Marketing and Release


### TODO Marketing Strategy

-   Describe how you intend to promote the game (social media, trailers, etc.)


### TODO Release Plan

-   Discuss the timeline for development, beta testing, and launch.


<a id="orge7fb754"></a>

## Post-Launch


### TODO Updates and Patches

-   Discuss plans for post-launch support, updates, and user feedback integration.


### TODO Community Engagement

-   Describe how you will engage with players after release.


<a id="org068f782"></a>

## TODO Miscellaneous

-   Any additional notes, inspirations, or ideas that don&rsquo;t fit elsewhere.


<a id="org16a2db1"></a>

## notes


### dignity

stolen from western astrology

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">sign</th>
<th scope="col" class="org-left">rules</th>
<th scope="col" class="org-left">exaltation</th>
<th scope="col" class="org-left">detriment</th>
<th scope="col" class="org-left">fall</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">aries</td>
<td class="org-left">mars</td>
<td class="org-left">sun</td>
<td class="org-left">venus</td>
<td class="org-left">saturn</td>
</tr>

<tr>
<td class="org-left">taurus</td>
<td class="org-left">venus</td>
<td class="org-left">moon</td>
<td class="org-left">mars</td>
<td class="org-left">none</td>
</tr>

<tr>
<td class="org-left">gemini</td>
<td class="org-left">mercury</td>
<td class="org-left">none</td>
<td class="org-left">jupiter</td>
<td class="org-left">none</td>
</tr>

<tr>
<td class="org-left">cancer</td>
<td class="org-left">moon</td>
<td class="org-left">jupiter</td>
<td class="org-left">saturn</td>
<td class="org-left">mars</td>
</tr>

<tr>
<td class="org-left">leo</td>
<td class="org-left">sun</td>
<td class="org-left">none</td>
<td class="org-left">saturn</td>
<td class="org-left">none</td>
</tr>

<tr>
<td class="org-left">virgo</td>
<td class="org-left">mercury</td>
<td class="org-left">mercury</td>
<td class="org-left">jupiter</td>
<td class="org-left">venus</td>
</tr>

<tr>
<td class="org-left">libra</td>
<td class="org-left">venus</td>
<td class="org-left">saturn</td>
<td class="org-left">mars</td>
<td class="org-left">sun</td>
</tr>

<tr>
<td class="org-left">scorpio</td>
<td class="org-left">mars</td>
<td class="org-left">none</td>
<td class="org-left">venus</td>
<td class="org-left">moon</td>
</tr>

<tr>
<td class="org-left">sagittarius</td>
<td class="org-left">jupiter</td>
<td class="org-left">none</td>
<td class="org-left">mercury</td>
<td class="org-left">none</td>
</tr>

<tr>
<td class="org-left">capricorn</td>
<td class="org-left">saturn</td>
<td class="org-left">mars</td>
<td class="org-left">moon</td>
<td class="org-left">jupiter</td>
</tr>

<tr>
<td class="org-left">aquarius</td>
<td class="org-left">saturn</td>
<td class="org-left">none</td>
<td class="org-left">sun</td>
<td class="org-left">none</td>
</tr>

<tr>
<td class="org-left">pisces</td>
<td class="org-left">jupiter</td>
<td class="org-left">venus</td>
<td class="org-left">mercury</td>
<td class="org-left">mercury</td>
</tr>
</tbody>
</table>


<a id="orgb54cbe8"></a>

# Links


<a id="org1b99a9d"></a>

## [VSCodium](https://vscodium.com)

It&rsquo;s basically VSCode but open-source
and without the annoying Microsoft telemetry stuff.


<a id="org24cd079"></a>

## org-mode

Consider using an `org-mode` extension (for `.org` files). It&rsquo;s a nice alternative to `markdown`, which is pretty limited.

