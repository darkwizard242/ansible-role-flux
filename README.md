[![build-test](https://github.com/darkwizard242/ansible-role-flux/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-flux/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-flux/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-flux/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/flux) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-flux&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-flux) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-flux&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-flux) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-flux&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-flux) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-flux?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-flux?color=orange&style=flat-square)

# Ansible Role: flux

Role to install (_by default_) [flux](https://github.com/fluxcd/flux2) on **Debian/Ubuntu** and **EL** systems. **flux** is an open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
flux_app: flux
flux_version: 2.7.3
flux_os: "{{ ansible_system | lower }}"
flux_architecture_map:
  amd64: amd64
  arm: arm64
  x86_64: amd64
  armv6l: armv6
  armv7l: armv7
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
flux_dl_url: https://github.com/fluxcd/flux2/releases/download/v{{ flux_version }}/{{ flux_app }}_{{ flux_version }}_{{ flux_os }}_{{ flux_architecture_map[ansible_architecture] }}.tar.gz
flux_bin_path: /usr/local/bin
flux_file_owner: root
flux_file_group: root
flux_file_permission_mode: '0755'
```

### Variables table:

Variable                  | Description
------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------
flux_app                  | Defines the app to install i.e. **flux**
flux_version              | Defined to dynamically fetch the desired version to install. Defaults to: **2.7.3**
flux_os                   | Defines os type.
flux_architecture_map     | Defines os architecture.
flux_dl_url               | Defines URL to download the flux binary from.
flux_bin_path             | Defined to dynamically set the appropriate path to store flux binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
flux_file_owner           | Owner for the binary file of flux.
flux_file_group           | Group for the binary file of flux.
flux_file_permission_mode | Defines the permission mode level for the file. Defaults to: `0755`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **flux**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.flux
```

For customizing behavior of role (i.e. specifying the desired **flux** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.flux
  vars:
    flux_version: 0.30.0
```

For customizing behavior of role (i.e. placing binary of **flux** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.flux
  vars:
    flux_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-flux/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
