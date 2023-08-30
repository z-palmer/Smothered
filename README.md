## **Notes for developer**

Make sure to throttle dynos up and down to save money on test deployment with:

`heroku ps:scale web=0 -a smothered`

then back up to

`heroku ps:scale web=1 -a smothered`

Color scheme from BandCamp for styling:

<ul>
<span style="color: #164B2F;"><li>BODY COLOR: #164B2F</li></span>
<span style="color: #ED8CC9;"><li>TEXT COLOR 1: #ED8CC9</li></span>
<span style="color: #C0F2C3;"><li>TEXT COLOR 2: #C0F2C3</li></span>
<span><li>LINK COLOR: #FFFFFF</li></span>
<span style="color: #C776FF;"><li>BG COLOR: #C776FF</li></span>
<span style="color: #E55DB2;"><li>NAV BAR COLOR: #E55DB2</li></span>
</ul>

**MAKE SURE TO REPLACE KEYS AND TOKENS BETWEEN PRODUCTION AND DEVELOPMENT**
Ensure they are in your 'Config Vars' in Heroku

In Python: os.environ.get('KEY')
In JavaScript: var key = process.env.KEY;

NEXT VERSION:

- Instagram tiles
- Music video and social links at bottom of page
- New fonts
- Song plays on landing page




