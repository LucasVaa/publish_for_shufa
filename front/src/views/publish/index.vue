<template>
  <div class="form-container">
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :md="12" :lg="8" :xl="8">
        <el-form
          ref="ruleForm"
          :model="ruleForm"
          :rules="rules"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="书法缩略图" prop="imageUrl">
            <el-upload
              class="avatar-uploader"
              action="http://10.10.1.124:8000/uploadfile"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload"
            >
              <img v-if="imageUrl" :src="imageUrl" class="avatar" />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
          <el-form-item label="书法原图" prop="fileUrl">
            <el-upload
              class="upload-demo"
              drag
              action="http://10.10.1.124:8000/uploadfile"
              multiple
              :on-success="handleFileSuccess"
            >
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                将文件拖到此处，或
                <em>点击上传</em>
              </div>
            </el-upload>
          </el-form-item>
          <el-form-item label="版权" prop="copyright">
            <el-select
              v-model="ruleForm.copyright"
              placeholder="请选择版权类型"
            >
              <el-option label="弱版权" value="weak"></el-option>
              <el-option label="强版权" value="strong"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="名称" prop="title">
            <el-input v-model="ruleForm.title"></el-input>
          </el-form-item>
          <el-form-item label="朝代" prop="date">
            <el-input v-model="ruleForm.date"></el-input>
          </el-form-item>
          <el-form-item label="作者" prop="creator">
            <el-input v-model="ruleForm.creator"></el-input>
          </el-form-item>
          <el-form-item label="出版社" prop="publisher">
            <el-input v-model="ruleForm.publisher"></el-input>
          </el-form-item>
          <el-form-item label="字体" prop="type">
            <el-input v-model="ruleForm.type"></el-input>
          </el-form-item>
          <el-form-item label="出处" prop="source">
            <el-input v-model="ruleForm.source"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">
              发布
            </el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'Form',
    data() {
      return {
        imageUrl: '',
        fileUrl: '',
        ruleForm: {
          title: '',
          date: '',
          creator: '',
          publisher: '',
          type: '',
          source: '',
          name: '',
          copyright: '',
          imageUrl: '',
          fileUrl: '',
        },
        rules: {
          title: [
            { required: true, message: '请输入字体名称', trigger: 'blur' },
            {
              min: 1,
              max: 1,
              message: '长度 1 个字符',
              trigger: 'blur',
            },
          ],
          imageUrl: [
            { required: true, message: '请上传字体缩略图', trigger: 'blur' },
          ],
          fileUrl: [
            { required: true, message: '请上传字体原图', trigger: 'blur' },
          ],
          copyright: [
            { required: true, message: '请选择版权类型', trigger: 'blur' },
          ],
        },
      }
    },
    methods: {
      submitForm(formName) {
        if (this.ruleForm.copyright == 'weak') {
          this.ruleForm.fileUrl = 'defa'
        }
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!')
          } else {
            return false
          }
        })
      },
      resetForm(formName) {
        this.$refs[formName].resetFields()
      },
      handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw)
        this.ruleForm.imageUrl = this.imageUrl
      },
      handleFileSuccess(res, file) {
        this.fileUrl = URL.createObjectURL(file.raw)
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg'
        const isLt2M = file.size / 1024 / 1024 < 2

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!')
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!')
        }
        return isJPG && isLt2M
      },
    },
  }
</script>

<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409eff;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
