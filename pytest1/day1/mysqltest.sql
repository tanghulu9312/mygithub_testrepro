CREATE TABLE dynamic_disaster_item(
  id int(10) not null auto_increment primary key comment 'ID主键（自动增长）',
  year varchar(4) comment '年份',
  county_code varchar(6) comment '行政区代码',
  previous_road_code VARCHAR(10) comment '原有路线编码',
  previous_start_mileage int(10) comment '原有起点桩号',
  previous_end_mileage int(10) comment '原有终点桩号',
  skill_level varchar(10) comment '技术等级',
  road_code varchar(20) comment '路线编码',
  start_mileage decimal(10,3) comment '起点桩号',
  end_mileage decimal(10,3) comment '终点桩号',
  mileage decimal(10,3) comment '里程',
  disaster_type VARCHAR(20) comment '灾毁类型',
  disaster_time date comment '灾毁时间',
  road_level varchar(10) comment '路线行政等级',
  disaster_level varchar(10) comment '灾毁等级',
  interdiction_road tinyint(1) comment '阻断路',
  rescue tinyint(1) comment '防汛抢险',
  other_losses DECIMAL(10,2) comment '其它损失',
  losses DECIMAL(10,2) comment '损失金额',
  img_name VARCHAR(20) comment '上传灾毁图片名字',
  img_url VARCHAR(50) comment '上传灾毁图片地址',
  video_name VARCHAR(20) comment '上传灾毁视频名字',
  video_ VARCHAR(50) comment '上传灾毁视频地址',
  loss_situation text(500) comment '灾毁损失情况',
  trial_loss_situation text(500) comment '审核后的灾毁损失情况',
  subgrade_mileage decimal(10,3) comment '路基（km）',
  subgrade_area decimal(10,1) comment '路基（平方米）',
  asphalt_mileage decimal(10,3) comment '路面类型（沥青砼路面）里程（km）',
  asphalt_area decimal(10,1) comment '路面类型（沥青砼路面）面积（平方米）',
  cement_mileage decimal(10,3) comment '路面类型（水泥砼路面）里程（km）',
  cement_area decimal(10,1) comment '路面类型（水泥砼路面）面积（平方米）',
  sand_mileage decimal(10,3) comment '路面类型（砂石路面）里程（km）',
  sand_area decimal(10,1) comment '路面类型（砂石路面）面积（平方米）',
  mileage_subtotal decimal(10,3) comment '路面类型（小计）里程（km）',
  are_subtotal decimal(10,1) comment '路面类型（小计）面积（km）',
  bridge_code VARCHAR(20) comment '桥梁代码',
  bridge_name VARCHAR(20) comment '桥梁名称',
  bridge_level VARCHAR(20) comment '桥梁技术等级',
  bridge_damage tinyint(1) comment '桥梁损毁程度',
  bridge_nature tinyint(1) comment '桥梁拟建性质',
  bridge_length DECIMAL (10,1) comment '桥梁长度(m)',
  bridge_width DECIMAL (10,1) comment '桥梁宽度（m）',
  bridge_center_pile_number int(10) comment '桥梁中心桩号',
  bridge_longitude DECIMAL(12,8) comment '桥梁中心点经度',
  bridge_latitude DECIMAL(12,8) comment '桥梁中心点纬度',
  bridge_custody VARCHAR(10) comment '管养单位',
  tunnel_damage tinyint(1) comment '隧道损毁程度',
  tunnel_length DECIMAL(10,1) comment '隧道长度（m）',
  tunnel_nature tinyint(1) comment '隧道拟建性质',
  tunnel_width decimal(10,1) comment '隧道宽度(m)',
  culvert_totalled int(10) comment '涵洞全毁（道）',
  culvert_subtotal int(10) comment '涵洞局部毁（道）',
  slope_cube DECIMAL(10,2) comment '防护工程（护坡方量）m³',
  slope_number int(10) comment '防护工程（护坡数量）处',
  bank_cube DECIMAL(10,2) comment '防护工程（驳岸方量）m³',
  bank_number int(10) comment '防护工程（驳岸数量）处',
  wall_cube DECIMAL(10,2) comment '防护工程（挡土墙方量）m³',
  wall_number int(10) comment '防护工程（挡土墙数量）处',
  protect_cube DECIMAL(10,2) comment '防护工程（小计方量）m³',
  protect_number int(10) comment '防护工程（小计数量）处',
  collapse DECIMAL(10,2) comment '坍塌方（m³）',
  flood_damage int(10) comment '水毁房屋（幢）',
  interdiction_degree tinyint(1) comment '阻断程度',
  company VARCHAR(10) comment '单位(m、m²、m³、座)',
  number DECIMAL(10,2) comment '数量',
  interdiction_time date comment '阻断或发生时间',
  recovery_time date comment '预计或实际恢复交通时间',
  interdiction_reason text(500) comment '阻断原因',
  measures text(500) comment '抢修措施',
  personnel_number int(10) comment '人员数量（工日）',
  personnel_money int(10) comment '人员金额（元）',
  vehicle_number  int(10) comment '车辆数量（台班）',
  vehicle_money int(10) comment '车辆金额（元）',
  equipment_number int(10) comment '施工设备数量（台班）',
  equipment_money int(10) comment '施工设计金额（元）',
  pve_subtotal int(10) comment '人员、车辆、施工设备金额小计（元）',
  cement_number decimal(10,3) comment '水泥数量（t）',
  cement_money int(10) comment '水泥金额（元）',
  gallet_number decimal(10,2) comment '碎石数量（m³）',
  gallet_money int(10) comment '碎石金额（元）',
  sand_number decimal(10,2) comment '砂数量（m³）',
  sand_money int(10) comment '砂金额（元）',
  cloth_number decimal(10,1) comment '彩布条数量（m²）',
  cloth_money int(10) comment '彩布条金额（元）',
  cgsc_subtotal int(10) comment '水泥、碎石、砂、彩布条金额小计（元）',
  other_resources int(10) comment '其他物资（元）',
  total_investment int(10) comment '总投入金额（元）',
  remark text(500) comment '备注',
  submit_level VARCHAR(10) comment '报送状态',
  mark tinyint(1) comment '标记',
  province_read tinyint(1) comment '省厅已阅',
  department_read tinyint(1) comment '省局已阅',
  deny_reason tinyint(1) comment '驳回原因',
  create_time datetime comment '创建时间',
  update_time datetime comment '更新时间',
  valid bit comment '有效性'
);

CREATE TABLE dynamic_upload_img(
    id int(10) not null auto_increment primary key comment 'ID主键（自动增长）',
    relation_id int(10) comment '关联主表ID',
    create_time datetime comment '创建时间',
    update_time datetime comment '更新时间',
    project_type int(2) comment '工程类型',
    project_stage int(2) comment '工程阶段',
    type int(2) comment '类型',
    url varchar(255) comment 'url地址',
    url_name varchar(255) comment '图片名称'
);























