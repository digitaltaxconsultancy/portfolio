import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    cartItems :[],
    totalItemsPrice:0,
    totalItems :0,
    totalQuantity: 0
}

const cartSlice = createSlice({

    name:"cartSlice",
    initialState,
    reducers:{

    }
})

export default cartSlice.reducer;