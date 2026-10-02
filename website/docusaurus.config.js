/**
 * Docusaurus configuration for the R2K16 codebase documentation.
 *
 * Base URL note:
 *  - GitHub Pages project sites are served from a sub-path (/R2K16/), which is
 *    the default here.
 *  - When running a local preview at the root of a host (e.g. a sandbox
 *    preview), override it with:
 *        DOCUSAURUS_BASE_URL=/ npm run build && DOCUSAURUS_BASE_URL=/ npm run serve
 *    (or simply `npm run start`, the dev server always handles this fine).
 */
const baseUrl = process.env.DOCUSAURUS_BASE_URL || '/R2K16/';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'R2K16 Docs',
  tagline: 'Codebase documentation for R2K16 — the modded 2016 Roblox engine',
  favicon: 'img/favicon.svg',

  // GitHub Pages (project pages live under /<repo-name>/)
  url: 'https://havaianasdestruido.github.io',
  baseUrl,

  // GitHub repo
  organizationName: 'havaianasdestruido',
  projectName: 'R2K16',

  onBrokenLinks: 'throw',

  themes: ['@docusaurus/theme-mermaid'],

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/docs',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/havaianasdestruido/R2K16/edit/main/website/',
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Color mode toggle
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },

      navbar: {
        title: 'R2K16',
        logo: {
          alt: 'R2K16 logo',
          src: 'img/logo.svg',
        },
        items: [
          { type: 'docSidebar', sidebarId: 'docs', label: 'Docs', position: 'left' },
          {
            type: 'doc',
            docId: 'architecture/index',
            label: 'Architecture',
            position: 'left',
          },
          {
            type: 'doc',
            docId: 'modules/index',
            label: 'Modules',
            position: 'left',
          },
          {
            type: 'doc',
            docId: 'reference/repo-map',
            label: 'Reference',
            position: 'left',
          },
          {
            href: 'https://github.com/havaianasdestruido/R2K16',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },

      footer: {
        style: 'dark',
        links: [
          {
            title: 'Documentation',
            items: [
              { label: 'Introduction', to: '/docs/intro' },
              { label: 'Getting Started', to: '/docs/getting-started/' },
              { label: 'Architecture', to: '/docs/architecture/' },
              { label: 'Module Reference', to: '/docs/modules/' },
            ],
          },
          {
            title: 'Development',
            items: [
              { label: 'Build (Windows)', to: '/docs/getting-started/building-windows' },
              { label: 'Build (CMake)', to: '/docs/getting-started/building-cmake' },
              { label: 'CI / CD', to: '/docs/development/ci' },
              { label: 'Maintaining This Site', to: '/docs/development/docs-site' },
            ],
          },
          {
            title: 'Project',
            items: [
              { label: 'GitHub', href: 'https://github.com/havaianasdestruido/R2K16' },
              { label: 'Roadmap', to: '/docs/reference/roadmap' },
              { label: 'Glossary', to: '/docs/reference/glossary' },
              { label: 'License (Apache-2.0)', href: 'https://github.com/havaianasdestruido/R2K16/blob/main/LICENSE' },
            ],
          },
        ],
        copyright: `Copyright © 2003-2016 Roblox Corporation (original engine) · R2K16 fork maintained by havaianasdestruido. Docs built with Docusaurus.`,
      },

      prism: {
        theme: require('prism-react-renderer').themes.github,
        darkTheme: require('prism-react-renderer').themes.dracula,
        additionalLanguages: ['lua', 'cmake', 'ini', 'bash'],
      },

      docs: {
        sidebar: {
          autoCollapseCategories: true,
        },
      },

      mermaid: {
        theme: {
          light: 'neutral',
          dark: 'dark',
        },
      },
    }),
};

module.exports = config;
