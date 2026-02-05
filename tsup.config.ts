import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['cli.ts'],
  format: ['esm'],
  clean: true,
  splitting: false, // 禁用代码分割，确保生成单一可执行文件
  treeshake: true, // 启用 tree shaking
  target: 'es2022',
  minify: false, // 禁用压缩以保留 shebang
  platform: 'node',
  shims: true, // 添加 Node.js shims
  esbuildOptions(options) {
    options.charset = 'utf8' // 添加这行来保留中文字符
    options.define = {
      'process.env.VERSION': `"${require('./package.json').version}"`,
      'process.env.IS_BUILD': "true"
    }
  }
})
