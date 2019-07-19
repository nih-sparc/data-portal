<template>
  <el-dialog :show-close="true" :visible.sync="visible" @open="onOpen" @close="onClose">
    <div class="header">
      <h2>Send Us a Message</h2>
    </div>
    <dialog-body>
      <el-form ref="contactForm" :label-position="labelPosition" label-width="100px" :model="contactUsForm" :rules="contactUsFormRules">
        <el-form-item prop="name" label="Your Name">
          <el-input required aria-placeholder="Enter your name" v-model="contactUsForm.name"></el-input>
        </el-form-item>
        <el-form-item prop="email" label="Your Email">
          <el-input aria-placeholder="Enter your email" type="email" v-model="contactUsForm.email"></el-input>
        </el-form-item>
        <el-form-item prop="message" label="Your Message">
          <el-input
            required
            aria-placeholder="Your message"
            type="textarea"
            v-model="contactUsForm.message"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button class="send-button" @click="submitContactForm">Send</el-button>
        </el-form-item>
      </el-form>
    </dialog-body>
  </el-dialog>
</template>

<script>

const contactForm = {
  name: null,
  email: null,
  message: null,
}

export default {
  name: "ContactUsModal",
  data() {
    return {
      labelPosition: "top",
      contactUsForm: {
        name: "",
        email: "",
        message: ""
      },
      contactUsFormRules: {
        name: [
          {
            required: true,
            message: 'Please enter your name',
            trigger: 'change'

          }
        ],

        email: [
          {
          required: true,
          message: 'Please enter your email',
          trigger: 'change'
        }
        ],

        message: [
          {
          required: true,
          message: 'Please enter a message',
          trigger: 'change'
        }
        ]

      },
    }
  },
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },

  methods: {
    submitContactForm: function() {
      this.$refs.contactForm.validate(valid => {
        if (!valid) {
          return;
        }
        this.sendRequest();
      });
    },

    sendRequest: function() {
      // send request logic goes here
      this.$http.post("/api/contact", {
        name: this.contactUsForm.name,
        email: this.contactUsForm.email,
        message: this.contactUsForm.message
      })
      this.onClose()
    },

    onClose: function(){
      this.$emit('on-close-dialog')
    },

    onOpen: function() {
      this.contactForm = Object.assign({}, contactForm)
    }
  }
};
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
  margin-left: 1px;
}

h2 {
  color: #24245b;
  font-weight: normal;
  font-size: 46px;
  line-height: 46px;
  padding-top: 148px;
  padding-bottom: 32px;
  width: 117%;
  text-transform: none;
}

/deep/ .el-dialog {
  width: 1280px;
  height: 800px;

  .el-dialog__body {
    background-color: #edf1fc;
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
  height: 80px;
  .el-textarea__inner {
    border-radius: 4px;
    border: 1px solid #909399;
  }
}

/deep/ .el-form {
  .el-form-item {
    .el-form-item__label {
      text-transform: none;
    }
  }
}
</style>