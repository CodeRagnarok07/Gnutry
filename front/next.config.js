/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // output: 'export',
  // distDir: 'static',
  trailingSlash: true,
  images: {
    unoptimized: true
  }
}

module.exports = nextConfig
