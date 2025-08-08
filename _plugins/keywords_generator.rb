require 'bibtex'

module Jekyll
  class KeywordsGenerator < Generator
    safe true
    priority :high

    def generate(site)
      scholar_config = site.config['scholar']
      bib_file = File.join(site.source, scholar_config['source'], scholar_config['bibliography'])

      return unless File.exist?(bib_file)

      bib = BibTeX.open(bib_file)
      pubs_by_keyword = Hash.new { |h, k| h[k] = [] }

      bib.each do |entry|
        next unless entry.key?('keywords')

        # The jekyll-scholar plugin uses the entry key as the id
        # and we need it to generate the bibliography entry.
        proc_entry = entry.convert_to_citeproc
        proc_entry['id'] = entry.key

        keywords = entry.keywords.split(',').map(&:strip)
        keywords.each do |keyword|
          pubs_by_keyword[keyword] << proc_entry
        end
      end

      pubs_by_keyword.each do |keyword, pubs|
        pubs.sort_by! do |p|
          [
            p.fetch('year', 0).to_i,
            p.fetch('volume', 0).to_i,
            p.fetch('number', 0).to_i
          ]
        end.reverse!
      end

      sorted_keywords = pubs_by_keyword.keys.sort_by do |keyword|
        pubs = pubs_by_keyword[keyword]
        most_recent_year = pubs.map { |p| p.fetch('year', 0).to_i }.max || 0
        [pubs.size, most_recent_year]
      end.reverse

      site.data['publications_by_keyword'] = pubs_by_keyword
      site.data['sorted_keywords'] = sorted_keywords
    end
  end
end
