<template>
  <el-dialog class="contact-modal" :show-close="true" :visible.sync="visible" @close="onClose">
    <div class="dialog-body">
      <div class="header">
        <h2>Send Us a Message</h2>
      </div>
      <el-form ref="contactForm" :label-position="labelPosition" label-width="100px" :model="contactUsForm" :rules="contactUsFormRules">
        <el-form-item prop="name" label="Your Name">
          <el-input aria-placeholder="Enter your name" v-model="contactUsForm.name"></el-input>
        </el-form-item>
        <el-form-item prop="email" label="Your Email">
          <el-input aria-placeholder="Enter your email" type="email" v-model="contactUsForm.email"></el-input>
        </el-form-item>
        <el-form-item prop="message" label="Your Message">
          <el-input
            aria-placeholder="Your message"
            type="textarea"
            v-model="contactUsForm.message"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button class="send-button" @click="submitContactForm">Send</el-button>
        </el-form-item>
      </el-form>
    </div>
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
      this.$emit('update:visible', false)
      this.$refs.contactForm.resetFields();
    },

  }
};
</script>

<style lang="scss" scoped>
@import '../../styles/_contact-modal.scss';
</style>
