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
      input: "src/index.ts",
      output: {
        dir: "static",
        // file: "./static/vendor.js",
        format: "es",
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
