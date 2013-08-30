# -*- ruby -*-

require 'rake'

task :default => [:setupenv]

TIMELY_ENV = ENV.fetch('TIMELY_ENV', 'local')
ENV_WRAPPER = "ops/timely-env.sh"

task :setupenv do
    sh "#{ENV_WRAPPER} pip install -r requirements/#{TIMELY_ENV}.txt"
end

def manage(args = "")
    sh "#{ENV_WRAPPER} python application/manage.py #{args} --settings=timely.settings.#{TIMELY_ENV}"
end

task :manage, [:task_with_args] do |t, args|
    args.with_defaults(:task_with_args => "test")
    manage args[:task_with_args]
end

[:runserver, :test].each do |manager_task|
    task manager_task do
        manage manager_task.id2name
    end
end

task :migrate, [:app] do |t, args|
    manage("schemamigration #{args[:app]} --auto")
    manage("migrate #{args[:app]}")
end
