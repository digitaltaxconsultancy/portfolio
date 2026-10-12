
import { useDispatch, useSelector } from 'react-redux';
import './_cat-nav.scss';
import { getCategories } from '../../Redux/Category/actions';
import { useEffect } from 'react';

const CatNav = () => {

    const categories = useSelector(
        state => state.categoryReducer.categories
    );

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getCategories());
    }, [dispatch]);

    //console.log("Categories from Redux:", categories);

    return (
        <div className="cat-nav-container">
            <ul>
               {categories.map((category) => {
                    if (category.parent_category_id === null) {
                        return (
                            <li key={category.id} className="list-items">
                                <a href="#">
                                    {category.category}
                                </a>
                            </li>
                        );
                    }

                    return null;
                })}
            </ul>
        </div>
    );
};

export default CatNav;
