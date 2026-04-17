const fs = require("node:fs");

module.exports = {
  layout: "entry.njk",
  tags: "entries",
  permalink: "entries/{{ page.fileSlug | cleanSlug }}/",
  eleventyComputed: {
    // Extract the entry's H1 heading from the raw markdown so the index can
    // show the real title (e.g. "AetherHeal's theory of trust formation")
    // rather than a slug-derived approximation. Falls back to fileSlug.
    pageTitle: (data) => {
      if (!data.page || !data.page.inputPath) return "";
      try {
        const raw = fs.readFileSync(data.page.inputPath, "utf-8");
        const body = raw.replace(/^---\n[\s\S]*?\n---\n/, "");
        const m = body.match(/^#\s+(.+)$/m);
        return m ? m[1].trim() : data.page.fileSlug;
      } catch (e) {
        return data.page.fileSlug;
      }
    },
  },
};
