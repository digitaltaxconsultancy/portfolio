import { useDispatch, useSelector } from 'react-redux';
import './_products.scss';
import { useEffect } from 'react';
import { getProducts } from '../../Redux/Products/productAction';

const Products = () => {

    const productData = useSelector(state => state.pr.products);
    const cart = useSelector(state => state.cr);
    
    const dispatch = useDispatch();

   useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

    console.log("Products from Redux:", productData);
     console.log("cart:", cart);

    return (
        <div className='products-container'>
            {
             productData.map((product,key)=>{

                return(
                <div className=" p-3  product-card ">
                    <div className='product-image-container'>
                        <img className='product-image' src ={require('../../assets/images/shop/'+product.product_img)}/>
                    </div>
                    <div className='product-info'> 
                        <h5> <a href='#'>{product.product_name}</a></h5>
                        <p className='product-price'>${product.price}</p>
                        <div className='product-rating'>
                            <i className='fa fa-star'/>
                            <i className='fa fa-star'/>
                            <i className='fa fa-star'/>
                            <i className='fa fa-star'/>
                            <i className='fa fa-star'/>
                            
                        </div>   
                    </div>

                        <div className='my-3'>
                            <div className='cart-button'>
                            <div className='cart-icon-cotainer'>
                            <i className='fa fa-shopping-cart mx-4'/>
                            </div>
                            <div className='cart-text-container mx-3'>
                            <p>Add to Cart</p>
                            </div>


                            </div>
                        </div>


                </div>
                )
            })

        }
        </div>

    );
}

export default Products;