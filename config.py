import os
class config():
    input_dir = ''
    max_len = '128'
    pretrain_model_dir = ''
    home_dir = os.getcwd() + '/'
    data_dir = home_dir + 'raw_data/ske/'
    tf_serving_addr = '127.0.0.1:8501'
    bert_vocab_dir = home_dir + 'pretrained_model/chinese_wwm_ext_L-12_H-768_A-12/vocab.txt'
    bert_config_dir =home_dir + 'pretrained_model/chinese_wwm_ext_L-12_H-768_A-12/bert_config.json'
    class_model_dir = 'output/predicate_classification_model/epochs6/model.ckpt-6000'
    seq_model_dir = 'output/sequnce_labeling_model/epochs9/model.ckpt-85304'
    middle_out_dir = './output/predicate_infer_out'
    out_dir = './output/sequnce_infer_out/epochs9/ckpt22000'
    token_label = ["[Padding]", "[category]", "[##WordPiece]", "[CLS]", "[SEP]", "B-SUB", "I-SUB", "B-OBJ", "I-OBJ", "O"]  #id 0 --> [Paddding]
    #class_label =  ['所需检查', '推荐用药', '疾病症状', '治疗方式']
    class_label =  ['丈夫', '上映时间', '专业代码', '主持人', '主演', '主角', '人口数量', '作曲', '作者', '作词', '修业年限', '出品公司', '出版社', '出生地', '出生日期','创始人', '制片人', '占地面积', '号', '嘉宾', '国籍', '妻子', '字', '官方语言', '导演', '总部地点', '成立日期', '所在城市', '所属专辑', '改编自', '朝代', '歌手', '母亲', '毕业院校', '民族', '气候', '注册资本', '海拔', '父亲', '目', '祖籍', '简称', '编剧', '董事长', '身高', '连载网站','邮政编码', '面积', '首都']
    schema = {
    '父亲': [('人物', '人物')],
    '妻子': [('人物', '人物')],
    '母亲': [('人物', '人物')],
    '丈夫': [('人物', '人物')],
    '祖籍': [('地点', '人物')],
    '总部地点': [('地点', '企业')],
    '出生地': [('地点', '人物')],
    '目': [('目', '生物')],
    '面积': [('Number', '行政区')],
    '简称': [('Text', '机构')],
    '上映时间': [('Date', '影视作品')],
    '所属专辑': [('音乐专辑', '歌曲')],
    '注册资本': [('Number', '企业')],
    '首都': [('城市', '国家')],
    '导演': [('人物', '影视作品')],
    '字': [('Text', '历史人物')],
    '身高': [('Number', '人物')],
    '出品公司': [('企业', '影视作品')],
    '修业年限': [('Number', '学科专业')],
    '出生日期': [('Date', '人物')],
    '制片人': [('人物', '影视作品')],
    '编剧': [('人物', '影视作品')],
    '国籍': [('国家', '人物')],
    '海拔': [('Number', '地点')],
    '连载网站': [('网站', '网络小说')],
    '朝代': [('Text', '历史人物')],
    '民族': [('Text', '人物')],
    '号': [('Text', '历史人物')],
    '出版社': [('出版社', '书籍')],
    '主持人': [('人物', '电视综艺')],
    '专业代码': [('Text', '学科专业')],
    '歌手': [('人物', '歌曲')],
    '作词': [('人物', '歌曲')],
    '主角': [('人物', '网络小说')],
    '董事长': [('人物', '企业')],
    '成立日期': [('Date', '机构'), ('Date', '企业')],
    '毕业院校': [('学校', '人物')],
    '占地面积': [('Number', '机构')],
    '官方语言': [('语言', '国家')],
    '邮政编码': [('Text', '行政区')],
    '人口数量': [('Number', '行政区')],
    '所在城市': [('城市', '景点')],
    '作者': [('人物', '图书作品')],
    '作曲': [('人物', '歌曲')],
    '气候': [('气候', '行政区')],
    '嘉宾': [('人物', '电视综艺')],
    '主演': [('人物', '影视作品')],
    '改编自': [('作品', '影视作品')],
    '创始人': [('人物', '企业')]}
