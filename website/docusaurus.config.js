/**
 * Docusaurus configuration for the R2K16 codebase documentation.
 *
 * The docs are served from a sub-path of the GitHub Pages site:
 *   https://havaianasdestruido.github.io/R2K16/docs/
 * The primary webpage at https://havaianasdestruido.github.io/R2K16/ is a
 * separate Jekyll site (see the `site/` folder at the repository root).
 *
 * Base URL note:
 *  - The default here matches GitHub Pages (docs live under /R2K16/docs/).
 *  - When running a local preview at the root of a host (e.g. a sandbox
 *    preview), override it with:
 *        DOCUSAURUS_BASE_URL=/docs/ npm run build && DOCUSAURUS_BASE_URL=/docs/ npm run serve
 *    (or simply `npm run start`, the dev server always handles this fine).
 */
const baseUrl = process.env.DOCUSAURUS_BASE_URL || '/R2K16/docs/';

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
          // Docs-only mode: this Docusaurus app exists solely to serve the
          // docs. Combined with baseUrl '/R2K16/docs/' the docs are published
          // at https://havaianasdestruido.github.io/R2K16/docs/.
          routeBasePath: '/',
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
            href: 'https://havaianasdestruido.github.io/R2K16/',
            label: 'Homepage',
            position: 'right',
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
              { label: 'Introduction', to: '/' },
              { label: 'Getting Started', to: '/getting-started/' },
              { label: 'Architecture', to: '/architecture/' },
              { label: 'Module Reference', to: '/modules/' },
            ],
          },
          {
            title: 'Development',
            items: [
              { label: 'Build (Windows)', to: '/getting-started/building-windows' },
              { label: 'Build (CMake)', to: '/getting-started/building-cmake' },
              { label: 'CI / CD', to: '/development/ci' },
              { label: 'Maintaining This Site', to: '/development/docs-site' },
            ],
          },
          {
            title: 'Project',
            items: [
              { label: 'Homepage', href: 'https://havaianasdestruido.github.io/R2K16/' },
              { label: 'GitHub', href: 'https://github.com/havaianasdestruido/R2K16' },
              { label: 'Roadmap', to: '/reference/roadmap' },
              { label: 'Glossary', to: '/reference/glossary' },
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
