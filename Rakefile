# -*- ruby -*-

require 'rake'

task :default => [:setupenv]

TIMELY_ENV = ENV.fetch('TIMELY_ENV', 'local')
ENV_WRAPPER = "ops/timely-env.sh"

task :setupenv do
    sh "#{ENV_WRAPPER} pip install -r requirements/#{TIMELY_ENV}.txt"
end

task :manage, [:mtask] do |t, args|
    args.with_defaults(:mtask => "test")
    sh "#{ENV_WRAPPER} python application/manage.py #{args[:mtask]} --settings=timely.settings.#{TIMELY_ENV}"
end
