module Jekyll
  module TildeFilter
    def unescape_tilde(input)
      input.to_s.gsub(/%7E/i, '~')
    end
  end
end

Liquid::Template.register_filter(Jekyll::TildeFilter)
