<template>
    <div class="sparc-datasets">

        <sparc-dataset-filter @filterChanged="onFilterChanged" 
            v-bind:authors="uniqueContributors"
            v-bind:tags="uniqueTags"></sparc-dataset-filter>

        <el-row v-for="dataset in visibleDatasets" :key="dataset">
            <el-card shadow="never">
                <div class="card-content">
                    <el-col class="card-content__image">
                        <img src="https://picsum.photos/80/80" class="image"/>
                    </el-col>
                    <el-col>
                        <el-row class="card-content__heading">
                            <a href="https://app.blackfynn.io" target="_blank">{{ dataset.name }}</a>
                        </el-row>
                        <el-row class="card-content__description">
                            {{ dataset.description }}
                        </el-row>
                        <el-row class="card-content__authors">
                            {{ dataset.userFirstName }} {{ dataset.userLastName }}
                        </el-row>
                    </el-col>
                </div>
            </el-card>
        </el-row>
        <el-pagination
            layout="prev, pager, next"
            :total="filteredDatasets && filteredDatasets.length ? filteredDatasets.length : 0"
            v-bind:current-page.sync="currentPage"
            v-bind:page-size.sync="pageSize">
        </el-pagination>
    </div>
</template>

<script>

import { propOr, pathOr } from 'ramda'
import SparcDatasetFilter from '../sparc-dataset-filter/SparcDatasetFilter.vue'

export default {
    name: 'sparc-datasets',

    components: {
        SparcDatasetFilter
    },

    data() {
        return {
            currentDate: new Date(),
            datasets: [],
            currentPage: 1,
            pageSize:4,
            datasetFilter: null,
            uniqueContributors: [],
            uniqueTags: []
        };
    },
    computed: {
        visibleDatasets() {
            return this.filteredDatasets.slice((this.currentPage-1)*this.pageSize, this.currentPage*this.pageSize )
        },
        filteredDatasets() {
            if (this.datasetFilter !== null && this.datasets !== null) {
                return this.datasets.filter(dataset => {
                    
                    if (this.datasetFilter.type == 'content') {
                        const terms = this.datasetFilter.value.toLowerCase().trim().split(' ')
                        // Filter by name || description
                        const datasetName = propOr('', 'name', dataset).toLowerCase()
                        for( var i=0; i<terms.length; i++ ){
                            const nameIndex = datasetName.indexOf(terms[i])
                            if (nameIndex > -1) {
                                return true
                            }
                        }

                        const datasetDescription = propOr('', 'description', dataset).toLowerCase()
                        for( var i=0; i<terms.length; i++ ){
                            const descriptionIndex = datasetDescription.indexOf(terms[i])
                            if (descriptionIndex > -1) {
                                return true
                            }
                        }
                        
                        return false
                    } else if (this.datasetFilter.type == 'authors') {
                        // Filter by authors -- only search for full term and don't split
                        const term = this.datasetFilter.value.toLowerCase().trim()
                        const authorName = propOr('', 'userFirstName', dataset) + ' ' + propOr('', 'userLastName', dataset)
                        const authorIndex = authorName.toLowerCase().indexOf(term)

                        return authorIndex > -1

                    }
                })
            } else {
                return this.datasets
            }
        }
    },

    mounted () {
        this.axios
            .get('/api/datasets')
            .then(response => {
                this.datasets = response.data

                this.uniqueContributors = this.getUniqueContributors(this.datasets);

                console.log(this.datasets)
            })
            .catch(e => {
                console.log(e)
            })
    },
    props: {
        message: {
            type: String,
            default: 'The SPARC Portal will be coming soon (Summer 2019)!'
        }
        
    },
    methods: {
        onFilterChanged (value) {
            this.datasetFilter = value;
        },
        getUniqueContributors (datasets) {
            // From list of published datasets, get unique contributors
            var contributors = []
            for (var index in datasets) {
                const fullName = propOr('', 'userFirstName', datasets[index]) + ' ' + propOr('', 'userLastName', datasets[index])
                contributors.push(fullName)
            }
            const uniqueContributors = contributors.filter(this.onlyUnique)

            // Format for autocomplete
            var results = []
            for (var index in uniqueContributors) {
                results.push({"value": uniqueContributors[index]})
            }
            return results
        },
        onlyUnique (value, index, self) { 
            return self.indexOf(value) === index;
        }
        
    }

}
</script>

<style lang="scss" scoped>
@import '../../../../../static/css/_variables.scss';

.sparc-datasets {
    display: flex;
    flex-direction: column;
    padding: 8px;
    margin-right:50px;
}

.card-content {
    display: flex;
    color: $text-color;
    text-align: left;
    height: 80px;

    .card-content__heading {
        font-size: 15px;
        font-weight: 600;
        line-height: 20px;

        a {
            color: $text-color;
            text-decoration: none;
        }

        a:hover {
            color: $facial;
        }
    }

    .card-content__description {
        font-size: 12px;
        font-weight: 300;
    }

    .card-content__image {
        margin-right: 5px;
        flex:1;
    }

    .card-content__authors {
        font-size: 10px;
        font-style: italic;
        margin-top: 5px;
    }

}

</style>
