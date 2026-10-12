
import { useDispatch, useSelector } from 'react-redux';
import './_side-nav.scss';
import accordionSlice from '../../Redux/Accordion/accordionCatSlice';
import { useEffect } from 'react';
import { getCategories } from '../../Redux/Category/actions';


const SideNav = () =>{

    const accordionData= useSelector(state=>state.categoryReducer.categories);
    const dispatch =useDispatch();
    useEffect(()=>{
        dispatch(getCategories());
    },[]);
return( 
 
<div> 
 
    <div className='side-nav'> 
        <div className='section-title'> 
            <h3>Category</h3> 
 
        </div> 
 <div className='accordion'>

    {accordionData.map((accordionCategory, key) => {

        if(accordionCategory.parent_category_id===null){

        return (
            <div className='accordion-item individual-category' key={key}>

                <div className='accordion-header'>

                    <button
                        className='accordion-button'
                        type='button'
                        data-bs-toggle='collapse'
                        data-bs-target={`#collapse${key}`}
                    >
                        <div className='category-title'>
                            <a href='#'>
                                {accordionCategory.category}
                            </a>
                        </div>
                    </button>

            </div>
                <div 
                    id={`collapse${key}`} 
                    className="accordion-collapse collapse"
                >
                    <div className="accordion-body">
                        <ul>
                            {accordionData
                                .filter(
                                    (subCategory) =>
                                        accordionCategory.id === subCategory.parent_category_id
                                )
                                .map((subCategory) => (
                                    <li className="sub-items" key={subCategory.id}>
                                        <a href="#">
                                            {subCategory.category}
                                        </a>
                                    </li>
                                ))}
                        </ul>
                    </div>
                </div>

            </div>
        )
    }
    })}

</div>
 
    </div> 
 
</div> 
 
) 
 
} 
export default SideNav;
