require 'date'

module Jekyll
  class ServiceGenerator < Generator
    safe true
    priority :high

    def generate(site)
      service_file = File.join(site.source, '_data', 'service.yml')
      return unless File.exist?(service_file)

      service_data = YAML.safe_load(File.read(service_file))
      current_service = []
      upcoming_service = []
      all_service = {}

      today = Date.today
      three_months_later = Date.today >> 3

      service_data.each do |service|
        start_date_str = service['Start Date']
        end_date_str = service['End Date']

        start_date = Date.parse(start_date_str)
        end_date = end_date_str ? Date.parse(end_date_str) : nil

        # Current Service
        if end_date.nil? || (start_date <= today && end_date >= today)
          current_service << service
        end

        # Upcoming Service
        if start_date > today && start_date <= three_months_later
          upcoming_service << service
        end

        # All Service
        year = start_date.year
        all_service[year] ||= {}
        all_service[year][service['Role']] ||= []
        all_service[year][service['Role']] << service
      end

      # Sort current and upcoming services by start date
      current_service.sort_by! { |s| Date.parse(s['Start Date']) }
      upcoming_service.sort_by! { |s| Date.parse(s['Start Date']) }

      # Sort all_service by year descending
      all_service = all_service.sort.reverse.to_h

      # Sort roles within each year
      all_service.each do |year, roles|
        roles.each do |role, services|
          services.sort_by! { |s| Date.parse(s['Start Date']) }
        end
        all_service[year] = roles.sort.to_h
      end

      site.data['current_service'] = current_service
      site.data['upcoming_service'] = upcoming_service
      site.data['all_service'] = all_service
    end
  end
end
