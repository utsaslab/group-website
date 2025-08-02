module Jekyll
  module TildeFilter
    NBSP = [0xA0].pack('U')

    def unescape_tilde(input)
      input.to_s
           .gsub(/%7E|%C2%A0/i, '~')
           .gsub(NBSP, '~')
    end
  end
end

Liquid::Template.register_filter(Jekyll::TildeFilter)
