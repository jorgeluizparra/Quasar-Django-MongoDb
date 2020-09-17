<template>
<q-page class="q-pa-lg">
    <q-form @submit.prevent="save(formData)">
        <q-input lazy-rules :rules="[ val => val.length == 11 || 'Please insert only numbers!']" type="number" class="form" outlined v-model="formData.client_cpf" label="Client CPF (Only numbers)" />
        <q-input lazy-rules :rules="[ val => val.length > 0 || 'Required!']" type="number" step="0.01" class="form" outlined v-model="formData.total" label="Total" />
        <q-input lazy-rules :rules="[ val => val.length > 0 || 'Required!']" type="number" step="0.01" class="form" outlined v-model="formData.received" label="Received" />
        <q-btn type="submit" class="form q-mr-md" color="primary" label="Register / Update" />
        <q-btn @click="clearFields()" type="button" class="form" color="secondary" label="Clear fields" />
    </q-form>
    <div v-if="formData.bills_quantities" class="q-mt-md">
        <div class="text-h5 q-mt-lg">Change bills/Coins</div>
        <q-list v-show="transactions" class="q-mt-md" bordered separator>
            <div v-for="(bill, key) in formData.bills_quantities" :key="key">
                <q-item v-show="bill.quantity != 0" clickable v-ripple>
                    <q-item-section>
                        ({{bill.quantity}}) R${{bill.bill}}
                    </q-item-section>
                </q-item>
            </div>
        </q-list>
    </div>
    <div class="text-h5 q-mt-lg">Transactions history</div>
    <q-form @submit.prevent="getByCpf(cpf)">
        <q-input :rules="[ val => val.length == 11 || 'Please insert only numbers!']" type="text" class="form" outlined v-model="cpf" label="Client CPF (Only numbers)" />
        <q-btn type="submit" class="form q-mr-md" color="primary" label="Search" />
        <q-btn @click.prevent="getAll()" type="button" class="form" color="primary" label="Get all" />
    </q-form>
    <q-list v-if="transactions" class="q-mt-md" bordered separator>
        <q-item @click.stop="selectTransaction(transaction)" v-for="(transaction, key) in transactions" :key="key" clickable v-ripple>
            <q-item-section>
                <b>Received: {{transaction.received}} - Paid: {{transaction.total}} = Change: {{transaction.change}}</b>
                Client: {{transaction.client_cpf}}
            </q-item-section>
            <q-item-section side>
                <q-btn @click.stop="deleteItem(transaction.id, key)" class="gt-xs" color="red" size="12px" flat dense round icon="delete" />
            </q-item-section>
        </q-item>
    </q-list>
    <div v-else class="text-h6 q-mt-sm">No transactions!</div>
</q-page>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

export default {
    name: 'PageIndex',
    data() {
        return {
            formData: {
                client_cpf: '',
                total: '',
                received: ''
            },
            cpf: '',
            transactions: ''
        }
    },
    methods: {
        clearFields() {
            this.formData.client_cpf = ''
            this.formData.total = ''
            this.formData.received = ''
            this.formData.bills_quantities = ''
        },
        selectTransaction(transaction) {
            console.log(transaction)
            this.formData = transaction
        },
        save(formData) {
            if (!formData.id) {
                axios
                    .post('http://127.0.0.1:5000/transactions', formData)
                    .then(response => {
                        // console.log(response.data)
                        this.transactions.push(response.data)
                        this.formData.client_cpf = ''
                        this.formData.total = ''
                        this.formData.received = ''
                        this.formData.bills_quantities = response.data.bills_quantities
                    })
                    .catch(error => {
                        console.log(error)
                    })
            } else {
                axios
                    .put('http://127.0.0.1:5000/transactions/' + formData.id, formData)
                    .then(response => {
                        console.log(response.data)
                        this.formData = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        },
        deleteItem(id, key) {
            // console.log(id)
            // console.log(key)
            this.$q.dialog({
                title: 'Delete transaction',
                message: 'Are you sure?',
                cancel: true,
                persistent: true,
                ok: {
                    push: true,
                    color: 'negative'
                }
            }).onOk(() => {
                axios
                    .delete('http://127.0.0.1:5000/transactions/' + id)
                    .then(response => {
                        this.transactions.splice(key, 1)
                        console.log(response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }).onCancel(() => {
                // console.log('>>>> Cancel')
            })
        },
        getAll() {
            axios
                .get('http://127.0.0.1:5000/transactions')
                .then(response => {
                    // console.log(response.data)
                    this.transactions = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getByCpf(cpf) {
            // console.log(cpf)
            axios
                .get('http://127.0.0.1:5000/transactions/query?cpf=' + cpf)
                .then(response => {
                    if (response.data.length > 0) {
                        // console.log(response.data)
                        this.transactions = response.data
                    } else {
                        // console.log('No tansactions!')
                        this.transactions = ''
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    beforeMount() {
        this.getAll()
    },
}
</script>

<style lang="css">
.form {
    margin-top: 10px;
}
</style>
