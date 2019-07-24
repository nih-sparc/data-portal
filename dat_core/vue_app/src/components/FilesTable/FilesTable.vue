<template>
  <div class="files-table">
    <div class="breadcrumb-list">
      <a
        class="breadcrumb"
        href="#"
        @click.prevent="getDirectory('/')"
      >
        Root
      </a>

      <div class="breadcrumb"
        v-for="(item, idx) in breadcrumbs"
        :key="idx"
      >
        <span>/</span>
        <a
          class="breadcrumb-link"
          href="#"
          @click.prevent="breadcrumbNavigation(idx)"
        >
          {{ item }}
        </a>
      </div>
    </div>

    <div class="files-table-table">
      <el-table :data="data">
        <el-table-column
          fixed
          prop="name"
          label="Name"
          min-width="300"
        >
          <template slot-scope="scope">
            <template v-if="scope.row.type === 'Directory'">
              <a
                href="#"
                @click.prevent="getDirectory(`${path}${scope.row.name}/`)"
              >
                {{ scope.row.name }}
              </a>
            </template>

            <template v-else>
              {{ scope.row.name }}
            </template>
          </template>
        </el-table-column>
        <el-table-column
          prop="fileType"
          label="File type"
          width="120"
        >
          <template slot-scope="scope">
            <template v-if="scope.row.type === 'Directory'">
              Folder
            </template>

            <template v-else>
              {{ scope.row.fileType }}
            </template>
          </template>
        </el-table-column>
        <el-table-column
          prop="size"
          label="Size"
          width="120"
          :formatter="formatStorage"
        />
        <el-table-column
          align="right"
          fixed="right"
          label="Operation"
          min-width="100"
          width="100"
        >
          <template
            v-if="scope.row.type === 'File'"
            slot-scope="scope"
          >
            <el-dropdown
              trigger="click"
              @command="onCommandClick"
            >
              <el-button
                icon="el-icon-more"
                size="small"
              />
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item
                  :command="{
                    type: 'requestDownloadFile',
                    scope
                  }"
                >
                  Download
                </el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
  import {
    compose,
    isEmpty,
    join,
    reject,
    slice,
    split,
    propOr,
    last,
    defaultTo,
    pathOr
  } from 'ramda'
  import FormatStorage from '../../mixins/bf-storage-metrics/index'

  const dataDict = {
    '/': [
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "Directory",
        "name": "folder A"
      }
    ],

    '/folder A/': [
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "Directory",
        "name": "folder B"
      }
    ],

    '/folder A/folder B/': [
      {
        "type": "File",
        "name": "file name",
        "fileType": "jpg",
        "uri": "",
        "size": 1341354523
      },
      {
        "type": "Directory",
        "name": "folder B"
      }
    ]


  }

  export default {
    name: 'FilesTable',

    mixins: [
      FormatStorage
    ],

    data: function() {
      return {
        path: '/',
        data: []
      }
    },

    computed: {
      breadcrumbs: function() {
        return compose(
          reject(isEmpty),
          split('/')
        )(this.path)
      }
    },

    mounted: function () {
      this.getDirectory('/')
    },

    methods: {
      /**
       * Get contents of directory
       * @param {String} path
       */
      getDirectory: function (path) {
        this.data = dataDict[path]
        this.path = path

        // this.$http.get(url)
        //   .then(response => {
        //     this.data = response
        //   })
      },

      /**
       * Navigate to another directory via breadcrumb
       * @param {Integer} idx
       */
      breadcrumbNavigation: function (idx) {
        const itemIdx = idx + 1

        const path = compose(
          join('/'),
          slice(0, itemIdx)
        )(this.breadcrumbs)

        const fullPath = `/${path}/`

        if (fullPath != this.path) {
          this.getDirectory(fullPath)
        }
      },

      /**
       * Format storage column
       * @param {Object} row
       * @param {Object} column
       * @param {Number} cellValue
       * @returns {String}
       */
      formatStorage: function (row, column, cellValue) {
        return this.formatMetric(cellValue)
      },

      /**
       * On command click callback for dropdown
       * @param {Object} evt
       */
      onCommandClick: function (evt) {
        const scope = propOr({}, 'scope', evt)
        const type = propOr({}, 'type', evt)
        const handler = this[type]

        if (typeof handler === 'function') {
          handler(scope)
        }
      },

      /**
       * Download file
       * @param {Object} scope
       */
      requestDownloadFile: function(scope) {
        const filePath = compose(
          last,
          defaultTo([]),
          split('s3://blackfynn-discover-use1/'),
          pathOr('', ['row', 'uri']),
        )(scope)

        const fileName = pathOr('', ['row', 'name'], scope)

        const requestUrl = `/api/download?key=${filePath}`
        this.$http.get(requestUrl).then(
          response => {
            this.downloadFile(fileName, response.data)
          }
        )
      },

      /**
       * Create an `a` tag to trigger downloading file
       * @param {String} filename
       * @param {String} url
       */
      downloadFile: function(filename, url) {
        const el = document.createElement('a')
        el.setAttribute('href', url)
        el.setAttribute('download', filename)

        el.style.display = 'none'
        document.body.appendChild(el)

        el.click()

        document.body.removeChild(el)
      }
    }
  }
</script>

<style lang="scss" scoped>
.breadcrumb-list {
  display: flex;
}
.files-table-table {
  background: #fff;
  border: 1px solid rgb(228, 231, 237);
  padding: 16px;
}
</style>
