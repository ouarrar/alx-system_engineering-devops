# Postmortem: ALX System Engineering & DevOps Project Outage

## Overview

During the release of ALX's System Engineering & DevOps project 0x19, at approximately 06:00 Coordinated Universal Time (UTC), an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server resulted in `500 Internal Server Error`s instead of the expected response of an HTML file defining a simple Holberton WordPress site.

## Debugging Process

Bug debugger Brennan (BDB) encountered the issue at around 19:20 UTC and promptly proceeded to address it.

1. Checked running processes using `ps aux`. Two `apache2` processes - `root` and `www-data` - were properly running.

2. Explored the `/etc/apache2/sites-available` folder and confirmed that the web server was serving content from `/var/www/html/`.

3. Ran `strace` on the PID of the `root` Apache process in one terminal and curled the server in another. Unfortunately, `strace` provided no useful information.

4. Repeated step 3, this time on the PID of the `www-data` process, and success! `strace` revealed a `-1 ENOENT (No such file or directory)` error related to an attempt to access the file `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. Investigated files in the `/var/www/html/` directory using Vim pattern matching. Located the erroneous `.phpp` file extension in the `wp-settings.php` file (Line 137: `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).

6. Removed the trailing `p` from the line.

7. Tested another `curl` on the server, and it returned a 200 A-ok!

8. Wrote a Puppet manifest to automate fixing the error.

## Summary

In short, a typo was the culprit. The WordPress app encountered a critical error in `wp-settings.php` when trying to load the file `class-wp-locale.phpp`. The correct file name, located in the `wp-content` directory of the application folder, was `class-wp-locale.php`.

The patch involved a simple fix - removing the trailing `p` from the erroneous file extension.

## Prevention

This outage wasn't a web server error but an application error. To prevent similar outages:

* **Test, Test, Test:** Test the application before deploying to catch errors early.

* **Status Monitoring:** Enable an uptime-monitoring service like [UptimeRobot](https://uptimerobot.com/) to receive instant alerts upon website outage.

In response to this error, a Puppet manifest [0-strace_is_your_friend.pp](https://github.com/MedAmezzane/alx-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp) was written to automate fixing identical errors in the future. The manifest replaces any `phpp` extensions in the file `/var/www/html/wp-settings.php` with `php`.

But, of course, it will never occur again because we're programmers, and we never make errors! 😉