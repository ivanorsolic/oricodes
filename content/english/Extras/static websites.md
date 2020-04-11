+++
title = "Static websites"
menuTitle = "Static websites"
draft = false
weight=4

+++

- **A static web page is delivered to the user exactly as stored on the server.** 
- By contrast, a dynamic web page first has to be generated using a web application.
- Which of course means that static websites display the same web pages for every user, as opposed to dynamic websites which can dynamically generate sites tailored to their users (at a significant cost and overhead). 
- Static sites can still dynamically do stuff, but they have to do it at the user's end (e.g. using JavaScript).

{{% notice tip %}}

I'll briefly explain how some of it works in the background, but if you're not interested and just want a guide on how to make a website like this, feel free to skip to the link below.

{{% /notice %}}

# [**CLICK HERE TO SKIP**](https://ori.codes/extras/prerequisites/)

## What is a static site generator?

- Static site generators (SSG) build static websites using a source directory of files and templates. 
- Or in layman's terms, an SSG takes a file like a markdown document, and generates a static website/web page from it.

### So why should you use a static site and a static site generator? 

Netlify has a [pretty neat list](https://www.netlify.com/blog/2016/05/18/9-reasons-your-site-should-be-static/)  that I'll try to abbreviate below:

### Security:

- By having only static HTML/CSS/JS files you're very much minimizing your [attack surface](https://www.wikiwand.com/en/Attack_surface) compared to running a bunch of software like a [CMS](https://www.wikiwand.com/en/Content_management_system) (e.g. WordPress, Drupal) with its own [database](https://www.wikiwand.com/en/Database#/Database_management_system) being run in a [virtual machine](https://www.wikiwand.com/en/Virtual_machine) running some [OS](https://www.wikiwand.com/en/Operating_system)...

- That doesn't mean static sites don't have an attack surface at all though. They can, and do, depending on you. But by default, especially if you're a beginner, you have much better security out of the box, and I'll go through what to do to make sure it stays secure.

### Speed:

- Whenever someone visits your site, especially if you're using a [CDN](https://www.wikiwand.com/en/Content_delivery_network) (more on that later), the load speeds (e.g. [time-to-first-byte](https://www.wikiwand.com/en/Time_to_first_byte)) will be much faster (or at worst the same) than a [CMS](https://www.wikiwand.com/en/Content_management_system). 

- The reason behind this is that you're giving the browser exactly what it wants (which is static HTML/CSS/JS) as soon as it requests the site, since that is actually the only stuff you have on your server and there is no need to render it into static files before serving it to the viewer.

### Smaller footprint (Speed + Security + Price?):

- A static site can be hosted on any server that can just return HTML files. 
- Which means, you don't have to find hosting that provides machines running software specific to your site (e.g. PHP, MySQL, WordPress, Nginx/Apache, whatever Linux distro you'd like).
- Which means you don't have to worry about the hosting company (or you yourself) keeping all of the software and dependencies up to date.
- Which means that once you've set up your site, you can just focus on actually doing stuff you're interested with it (e.g. writing). It also means you'll get a lot more for a lot, lot cheaper ([even free!](https://www.netlify.com/)). 

### Scalability

- If you ever get to the sweet trouble of having much more visitors than you'd've expected, that won't be an issue at all if you're using a static site. 
- Scaling it up just means increasing your bandwidth with your provider, so more requests can be served, and it usually just means clicking a few buttons and paying a few bucks extra.

## What static site generator to use?

There sure is a bunch of them. And there are quite a few good ones. You can see a [list of them here](https://www.staticgen.com/), but **I'd recommend going with [Hugo](https://gohugo.io/)**. It has a friendly, active community that will help you out and it is really [well developed, fast](https://gohugo.io/about/features/) and as [secure as it gets](https://gohugo.io/about/security-model/). But you can use any other generator you'd like, the process is mostly the same and is just as straightforward for other SSGs.)

