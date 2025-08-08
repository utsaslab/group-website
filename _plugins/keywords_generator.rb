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
        next unless entry.respond_to?(:keywords) && entry.keywords

        # Manually create the hash for the template
        pub_hash = {}

        # Simple fields
        pub_hash['title'] = entry.title.to_s if entry.respond_to?(:title)
        pub_hash['year'] = entry.year.to_s if entry.respond_to?(:year)
        pub_hash['volume'] = entry.volume.to_s if entry.respond_to?(:volume)
        pub_hash['number'] = entry.number.to_s if entry.respond_to?(:number)
        pub_hash['booktitle'] = entry.booktitle.to_s if entry.respond_to?(:booktitle)
        pub_hash['journal'] = entry.journal.to_s if entry.respond_to?(:journal)
        pub_hash['publisher'] = entry.publisher.to_s if entry.respond_to?(:publisher)
        pub_hash['pdf'] = entry.pdf.to_s if entry.respond_to?(:pdf)
        pub_hash['doi'] = entry.doi.to_s if entry.respond_to?(:doi)
        pub_hash['slides'] = entry.slides.to_s if entry.respond_to?(:slides)
        pub_hash['video'] = entry.video.to_s if entry.respond_to?(:video)
        pub_hash['audio'] = entry.audio.to_s if entry.respond_to?(:audio)
        pub_hash['abstract'] = entry.abstract.to_s if entry.respond_to?(:abstract)
        pub_hash['type'] = entry.type.to_s
        pub_hash['file'] = entry.file.to_s if entry.respond_to?(:file)


        # Complex fields
        pub_hash['key'] = entry.key
        pub_hash['bibtex'] = entry.to_s

        # Author array
        if entry.respond_to?(:author) && entry.author
          author_array = []
          entry.author.each do |author|
            author_array << { 'first' => author.first, 'last' => author.last }
          end
          pub_hash['author_array'] = author_array
        end

        keywords = entry.keywords.to_s.split(',').map(&:strip)
        keywords.each do |keyword|
          pubs_by_keyword[keyword] << pub_hash
        end
      end

      # Sort publications within each keyword group
      pubs_by_keyword.each do |keyword, pubs|
        pubs.sort_by! do |p|
          [
            p.fetch('year', '0').to_i,
            p.fetch('volume', '0').to_i,
            p.fetch('number', '0').to_i
          ]
        end.reverse!
      end

      # Sort keywords
      sorted_keywords = pubs_by_keyword.keys.sort_by do |keyword|
        pubs = pubs_by_keyword[keyword]
        most_recent_year = pubs.map { |p| p.fetch('year', '0').to_i }.max || 0
        [pubs.size, most_recent_year]
      end.reverse

      site.data['publications_by_keyword'] = pubs_by_keyword
      site.data['sorted_keywords'] = sorted_keywords
    end
  end
end
