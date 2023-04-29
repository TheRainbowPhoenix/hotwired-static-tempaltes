import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  clearScreen: false,
  plugins: [
    // reactRefresh(),
  ],
  build: {
    target: "esnext",
    outDir: "static/",
    emptyOutDir: true,
    assetsDir: "",
    manifest: true,
    rollupOptions: {
      //   external: ["@hotwired/stimulus", "src_get"],
      input: {
        index: "src/index.ts",
        common: "src/seo.ts",
      },
      output: {
        dir: "static",
        // file: "./static/vendor.js",
        format: "es",
        entryFileNames: `[name].js`,
        chunkFileNames: `[name].js`,
        assetFileNames: `[name].[ext]`,
        manualChunks: {
          //   stimulus: ["@hotwired/stimulus"],
          //   turbo: ["@hotwired/turbo"],
          runtime: ["@hotwired/stimulus", "@hotwired/turbo"],
        },
      },
      //   output: {
      //     globals: {
      //       "@hotwired/stimulus": "Stimulus",
      //     },
      //   },
    },
  },

  root: "src",
});
