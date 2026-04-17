module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy(".nojekyll");

  // Eleventy's fileSlug strips the leading YYYY-MM-DD- date prefix automatically,
  // leaving e.g. "0001-aetherheal-theory-of-trust-formation". These filters strip
  // the remaining NNNN- and produce either a URL-friendly slug or a spaced fallback
  // title (only used when an entry's markdown has no H1).
  eleventyConfig.addFilter("cleanSlug", function (fileSlug) {
    return fileSlug.replace(/^\d+-/, "");
  });

  eleventyConfig.addFilter("slugToTitle", function (fileSlug) {
    return fileSlug.replace(/^\d+-/, "").replace(/-/g, " ");
  });

  eleventyConfig.addFilter("isoDate", function (value) {
    if (!value) return "";
    if (typeof value === "string") return value;
    const y = value.getUTCFullYear();
    const m = String(value.getUTCMonth() + 1).padStart(2, "0");
    const d = String(value.getUTCDate()).padStart(2, "0");
    return y + "-" + m + "-" + d;
  });

  eleventyConfig.addFilter("padId", function (value) {
    return String(value).padStart(4, "0");
  });

  return {
    dir: {
      input: ".",
      output: "docs",
      includes: "_includes",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    pathPrefix: "/errata/",
  };
};
