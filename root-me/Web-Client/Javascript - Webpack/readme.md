# Challenge: [Javascript - Webpack](https://www.root-me.org/en/Challenges/Web-Client/Javascript-Webpack)
**15 pts**

## Description
Do you know webpack?

## Solution
Hi! I haven’t played CTF challenges for a while, so this one took me some time to warm up :>

Since the challenge mentions **Webpack**, the first thing I did was to analyze the generated JavaScript bundle.  
While browsing through the files, I noticed that several `.js` files contained suspicious commented lines at the bottom:

`\webpack:\src\router\index.js`

```js
// ...
    // {
    //   path: '/you-will-not-find-this-route-because-it-is-hidden',
    //   name: 'YouWillNotFindThisRouteBecauseItIsHidden',
    //   component: QuackQuack
    // }
```
This looks like a hidden route, so my first idea was to try accessing it.
However, this route does not actually exist in the final build — the component name is wrong (**QuackQuack**), and the route is commented out.
So nothing useful here.

At this point I looked deeper into the project structure and noticed something more interesting:

<img src='./media/Screenshot 2025-11-16 113940.png'/>

Webpack had generated .map files. These files are meant for debugging and contain the original, unminified source code, including comments and variable names.

So I downloaded the **app.a92c5074dafac0cb6365.js.map** file and simply searched for keywords such as password or flag and found the real flag there.
