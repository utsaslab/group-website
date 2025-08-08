require 'jekyll/scholar'

module Jekyll
  class KeywordsGenerator < Generator
    safe true
    priority :low # Run after jekyll-scholar

    def generate(site)
      return if !site.config['scholar']

      scholar = site.scholar
      if !scholar || !scholar.bibliography
        return
      end

      pubs_by_keyword = Hash.new { |h, k| h[k] = [] }

      scholar.bibliography.each do |entry|
        next unless entry.respond_to?(:keywords) && entry.keywords

        keywords = entry.keywords.to_s.split(',').map(&:strip)
        keywords.each do |keyword|
          pubs_by_keyword[keyword] << entry
        end
      end

      # Sort publications within each keyword group
      pubs_by_keyword.each do |keyword, pubs|
        pubs.sort_by! do |p|
          [
            p.year.to_i,
            p.volume.to_i,
            p.number.to_i
          ]
        end.reverse!
      end

      sorted_keywords = pubs_by_keyword.keys.sort_by do |keyword|
        pubs = pubs_by_keyword[keyword]
        most_recent_year = pubs.map { |p| p.year.to_i }.max || 0
        [pubs.size, most_recent_year]
      end.reverse

      site.data['publications_by_keyword'] = pubs_by_keyword
      site.data['sorted_keywords'] = sorted_keywords
    end
  end
end
