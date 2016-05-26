require 'sinatra'
require 'sinatra/reloader'
require 'sqlite3'


# create table
sql = <<-SQL
  create table switch (
    id integer primary key,
    on_off integer
  );
SQL
db.execute(sql)

# insert
db.execute('insert into switch (on_off) values (0)';)


get '/switch' do
  btn_clicked(params[:switch])
  erb :switch
end

def btn_clicked(params)
  db = SQLite3::Database.new 'switch.db'
  # ボタンをクリックするとDB更新
  if params == "off"
    p "オフにする"
    db.execute('update switch set on_off = 0 where id = 1')
    p db.execute('select * from switch')
  else
    p "オンにする"
    db.execute('update switch set on_off = 1 where id = 1')
    # スイッチの確認
    p db.execute('select * from switch')
  end
end

get '/back_switch' do
  db = SQLite3::Database.new 'switch.db'
  #ボタンon_offの状態をselect
  @switch = db.execute('select on_off from switch where id = 1')
  erb :back_switch
end
