import React, { useState, useEffect } from 'react';
import axios from "axios";

const PaymentInfo = () => {
    const [payments, setPayments] = useState([]);

    useEffect(() => {
        const fetchPayments = async () => {
            const dtpToken = localStorage.getItem('REACT_APP_DTP_TOKEN');
            const oauth2Token = localStorage.getItem('REACT_APP_OAUTH2_TOKEN');

            let formData = new FormData();
            formData.append('dtp_token', oauth2Token);
            const response = await axios.get('http://localhost:8000/api/payment/get_payment', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Authorization': `Bearer ${oauth2Token}`
                }
            });

            if (response.ok) {
                const data = await response.json();
                setPayments(data);
            } else {
                console.error(`Failed to fetch payments: ${response.status}`);
            }
        };

        fetchPayments();
    }, []);

    const deletePayment = (dtpCode) => {
        setPayments(payments.filter(payment => payment.dtpCode !== dtpCode));
    };

    return (
        <table>
            <thead>
                <tr>
                    <th>DTP Code</th>
                    <th>User Name</th>
                    <th>Payment Value</th>
                    <th>Payment Type</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {payments.map(payment => (
                    <tr key={payment.dtpCode}>
                        <td>{payment.dtpCode}</td>
                        <td>{payment.userName}</td>
                        <td>{payment.paymentValue}</td>
                        <td>{payment.paymentType}</td>
                        <td>
                            <button onClick={() => deletePayment(payment.dtpCode)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default PaymentInfo;
