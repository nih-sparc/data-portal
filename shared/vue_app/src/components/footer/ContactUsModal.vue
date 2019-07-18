<template>
  <el-dialog :show-close="true" :visible.sync="visible" @open="resetForm">
    <div class="header">
       <h2>Send us a Message</h2>
    </div>
    <dialog-body>
      <el-form :label-position="labelPosition" label-width="100px" :model="contactUsForm">
        <el-form-item label="Your Name">
          <el-input aria-placeholder="Enter your name" v-model="contactUsForm.name"></el-input>
        </el-form-item>
        <el-form-item label="Your Email">
          <el-input aria-placeholder="Enter your email" type="email" v-model="contactUsForm.email"></el-input>
        </el-form-item>
        <el-form-item label="Your Message">
          <el-input aria-placeholder="Your message" type="textarea" height="60" v-model="contactUsForm.message"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button class="send-button">Send</el-button>
        </el-form-item>
      </el-form>
    </dialog-body>
  </el-dialog>
</template>

<script>
    export default {
        name: 'ContactUsModal',
        data() {
          return {
            labelPosition: 'top',
            contactUsForm: {
              name: '',
              email: '',
              message: ''
            }
          }
        },
        props: {
            visible: {
                type: Boolean,
                default: false
            },
        },
    }
</script>

<style lang="scss" scoped>

.send-button {
  display: flex;
  justify-content: center;
  background-color: #24245b;
  color: white;
  height: 40px;
  width: 128px;
  border-radius: 4px;
  margin-bottom: 148px;
  margin-left: 121px;
}

.header {
  margin-left: -15px;
}

h2 {
  color: #24245b;
  font-weight: normal;
  font-size: 46px;
  line-height: 46px;
  padding-top: 148px;
  padding-bottom: 32px;
  width: 117%;
}

/deep/ .el-dialog {
  width: 1280px;
  height: 800px;

  .el-dialog__body {
    background-color: #EDF1FC;
    padding-left: 441px;
    padding-right: 462px;
  }

  .el-dialog__header {
    padding: 0;
  }

  .el-dialog__headerbtn .el-dialog__close {
    font-size: 34px;
    color: #24245b;
    font-weight: bold;
  }
}

/deep/ .el-input {
  .el-input__inner {
    border-radius: 4px;
    border: 1px solid #909399;
  }
}

/deep/ .el-textarea {
  .el-textarea__inner {
    border-radius: 4px;
    border: 1px solid #909399;
  }
}
</style>