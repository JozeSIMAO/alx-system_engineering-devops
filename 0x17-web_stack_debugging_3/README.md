# Web Stack Debugging with Puppet

## Description

This project focuses on resolving a 500 Internal Server Error in Apache using the strace tool to identify the issue. The identified problem will be fixed manually and then automated using Puppet, adhering to the specified requirements.

## Task Details

### Task 0: Strace is Your Friend

- **Objective:** Use strace to find out why Apache is returning a 500 error. Fix the issue manually and then automate the solution using Puppet.
- **Requirements:**
  - Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
  - Puppet manifests must run without error.
  - Puppet manifests must end with the extension .pp.
  - Files will be checked with Puppet v3.4.
  - Your 0-strace_is_your_friend.pp file must contain Puppet code.

### Usage

1. **Install puppet-lint**

   ```bash
   $ apt-get install -y ruby
   $ gem install puppet-lint -v 2.1.1
