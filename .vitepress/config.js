import { defineConfig } from 'vitepress'
import { generateSidebar } from 'vitepress-sidebar'

// 自动化侧边栏路径修复函数
function generateSidebarWithCorrectPaths(routePrefix, scanStartPath, options = {}) {
  // 生成原始侧边栏
  const originalSidebar = generateSidebar({
    documentRootPath: '.',
    scanStartPath: scanStartPath,
    debugPrint: false,
    ...options
  })
  
  // 递归修复链接路径
  function fixPaths(items, prefix) {
    return items.map(item => {
      const newItem = { ...item }
      
      // 修复链接路径
      if (newItem.link && !newItem.link.startsWith(prefix)) {
        // 移除可能存在的前导斜杠，然后添加正确的前缀
        const cleanLink = newItem.link.replace(/^\/+/, '')
        newItem.link = `${prefix}${cleanLink}`
      }
      
      // 递归处理子项
      if (newItem.items && Array.isArray(newItem.items)) {
        newItem.items = fixPaths(newItem.items, prefix)
      }
      
      return newItem
    })
  }
  
  // 确保routePrefix以/开头和结尾
  const normalizedPrefix = routePrefix.startsWith('/') ? routePrefix : `/${routePrefix}`
  const finalPrefix = normalizedPrefix.endsWith('/') ? normalizedPrefix : `${normalizedPrefix}/`
  
  return fixPaths(originalSidebar, finalPrefix)
}

export default defineConfig({
  title: '古诗词智能文档',
  description: '利用智能技术处理古诗词文档的知识库，包含古诗词赏析、创作指导和智能化处理工具',
  
  // 设置源目录为docs
  srcDir: 'docs',
  
  // 忽略死链接检查
  ignoreDeadLinks: true,
  
  // 服务器配置
  vite: {
    server: {
      host: '0.0.0.0',
      port: 5173,
      strictPort: false,
      cors: true,
      fs: {
        strict: false,
        allow: ['..', '../..']
      },
      hmr: {
        port: 5173
      }
    },
    define: {
      __VUE_PROD_DEVTOOLS__: false
    }
  },
  
  // 主题配置
  themeConfig: {
    // 网站标题
    siteTitle: '古诗词智能文档',
    
    // 导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '山水田园', link: '/landscape/' },
      { text: '边塞征战', link: '/frontier/' },
      { text: '咏史怀古', link: '/history/' },
      { text: '抒情咏物', link: '/lyrical/' },
      { text: 'GitHub', link: 'https://github.com/yangbin09/gushici-intelligent-docs' }
    ],

    // 侧边栏 - 使用自动化路径修复的 vitepress-sidebar
    sidebar: {
      // 山水田园目录自动生成侧边栏
      '/landscape/': generateSidebarWithCorrectPaths('/landscape/', 'docs/landscape', {
        hyphenToSpace: true,
        underscoreToSpace: true,
        capitalizeFirst: true,
        capitalizeEachWords: true,
        collapsed: false,
        collapseDepth: 2,
        sortMenusByName: true,
        sortMenusOrderByDescending: false,
        frontmatterTitleFieldName: 'title'
      }),
      
      // 边塞征战目录自动生成侧边栏
      '/frontier/': generateSidebarWithCorrectPaths('/frontier/', 'docs/frontier', {
        hyphenToSpace: true,
        underscoreToSpace: true,
        capitalizeFirst: true,
        capitalizeEachWords: true,
        collapsed: false,
        collapseDepth: 2,
        sortMenusByName: true,
        sortMenusOrderByDescending: false,
        frontmatterTitleFieldName: 'title'
      }),
      
      // 咏史怀古目录自动生成侧边栏
      '/history/': generateSidebarWithCorrectPaths('/history/', 'docs/history', {
        hyphenToSpace: true,
        underscoreToSpace: true,
        capitalizeFirst: true,
        capitalizeEachWords: true,
        collapsed: false,
        collapseDepth: 2,
        sortMenusByName: true,
        sortMenusOrderByDescending: false,
        frontmatterTitleFieldName: 'title'
      }),
      
      // 抒情咏物目录自动生成侧边栏
      '/lyrical/': generateSidebarWithCorrectPaths('/lyrical/', 'docs/lyrical', {
        hyphenToSpace: true,
        underscoreToSpace: true,
        capitalizeFirst: true,
        capitalizeEachWords: true,
        collapsed: false,
        collapseDepth: 2,
        sortMenusByName: true,
        sortMenusOrderByDescending: false,
        frontmatterTitleFieldName: 'title'
      }),
      

    },

    // 搜索
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索文档',
            buttonAriaLabel: '搜索文档'
          },
          modal: {
            noResultsText: '无法找到相关结果',
            resetButtonTitle: '清除查询条件',
            footer: {
              selectText: '选择',
              navigateText: '切换'
            }
          }
        }
      }
    },

    // 社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/yangbin09/tera-docs' }
    ],

    // 页脚
    footer: {
      message: '基于 MIT 许可发布',
      copyright: 'Copyright © 2025 古诗词智能文档'
    },

    // 编辑链接
    editLink: {
      pattern: 'https://github.com/yangbin09/tera-docs/edit/master/docs/:path',
      text: '在 GitHub 上编辑此页面'
    },

    // 最后更新时间
    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'medium'
      }
    }
  },

  // 头部配置
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#3c82f6' }],
    ['meta', { name: 'og:type', content: 'website' }],
    ['meta', { name: 'og:locale', content: 'zh-CN' }],
    ['meta', { name: 'og:title', content: '古诗词智能文档' }],
    ['meta', { name: 'og:site_name', content: '古诗词智能文档' }],
    ['meta', { name: 'og:description', content: '包含各种AI写作指令和教程的文档集合，涵盖多种写作场景和应用' }]
  ],

  // 语言配置
  lang: 'zh-CN',

  // 清理URL
  cleanUrls: true,

  // Markdown配置
  markdown: {
    lineNumbers: true,
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    }
  }
})