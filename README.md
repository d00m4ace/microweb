# MicroWeb
Yet another Markdown-based static site/blog generator in Python, with automatic sitemap creation.

An example of a website created using MicroWeb is [d00m4ace.com](http://d00m4ace.com).

This project is a statistical website and blog generator written in pure Python and based on Markdown. Designed as an alternative to off-the-shelf engines such as HUGO, it offers a simple but effective code base for enthusiasts and developers who want more flexibility and control over the process of creating their websites and blogs. The project is ideal for those who want to learn the principles of static websites or create a unique website with minimal technical requirements and without having to rely on complex and extensive frameworks.

# MicroWeb Usage Guide

## 1. Installation
- Ensure Python is installed on your system.
- Download/clone the MicroWeb project from its repository.
- Install dependencies (if any) using pip.

## 2. Configuration
- Set up templates and site structure in the configuration. See: \site\test\pages.cfg and \site\test\posts.cfg
- Copy \site\test\webroot to \output directory.

## 3. Writing Content
- Create content using Markdown. Each page or blog post should be a separate Markdown file. See: \site\test\pages\ and \site\test\posts\

## 4. Generating the Site
- Run the microweb.py script to convert Markdown files into HTML.
- A sitemap file \output\sitemap.xml will be generated automatically during this process.

## 5. Previewing Your Site
- Preview the site \output locally by running a local server, if available.

## 6. Deployment
- Deploy the site \output to your hosting service. This could involve uploading files, pushing to a repository, or using a deployment tool.

## 7. Updating Your Site
- Modify or add new Markdown files for updates. See: \site\test\pages\ and \site\test\posts\
- Re-run the microweb.py script to regenerate the site.

![screenshot](https://d00m4ace.com/imgs/microweb.png)

